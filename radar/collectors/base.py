"""Socle commun des collecteurs : HTTP poli, limitation de débit, reprise sur erreur.

Principes éthiques et juridiques appliqués à la collecte automatisée :
  * privilégier les API officielles aux extractions de pages (scraping) ;
  * s'identifier (User-Agent explicite avec contact) ;
  * respecter les quotas annoncés par chaque service (ex. arXiv : 1 requête / 3 s) ;
  * ne collecter aucune donnée personnelle au-delà du strict nécessaire (RGPD, art. 5).
"""
from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from datetime import datetime
from urllib.parse import urlsplit

import requests

from radar.models import Signal

log = logging.getLogger(__name__)

USER_AGENT = "radar-veille-ia/1.0 (usage pedagogique; contact: veille@example.org)"


class PoliteSession:
    """Session HTTP respectant un intervalle minimal entre deux requêtes vers un même hôte."""

    def __init__(self, min_interval: dict[str, float] | None = None, retries: int = 3, timeout: float = 30):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self.min_interval = min_interval or {}
        self.retries = retries
        self.timeout = timeout
        self._last_call: dict[str, float] = {}

    def get(self, url: str, **kwargs) -> requests.Response:
        host = urlsplit(url).netloc
        for attempt in range(self.retries + 1):
            wait = self.min_interval.get(host, 0) - (time.monotonic() - self._last_call.get(host, 0))
            if wait > 0:
                time.sleep(wait)
            self._last_call[host] = time.monotonic()
            try:
                resp = self.session.get(url, timeout=self.timeout, **kwargs)
            except requests.ConnectionError as exc:
                log.warning("connexion impossible à %s (%s), tentative %d", host, exc, attempt + 1)
            else:
                if resp.status_code < 400:
                    return resp
                if resp.status_code not in (403, 429) and resp.status_code < 500:
                    resp.raise_for_status()   # 4xx non transitoire : inutile d'insister
                log.warning("HTTP %d sur %s, tentative %d", resp.status_code, host, attempt + 1)
                if (delay := _quota_delay(resp)) is not None:
                    log.info("quota atteint sur %s : attente de %.0f s", host, delay)
                    time.sleep(delay)
                    continue
            time.sleep(2 ** attempt * 2)      # repli exponentiel : 2 s, 4 s, 8 s…
        raise RuntimeError(f"échec de la collecte sur {host} après {self.retries + 1} tentatives")


def _quota_delay(resp: requests.Response, cap: float = 120) -> float | None:
    """Délai imposé par le service (en-têtes Retry-After ou X-RateLimit-Reset), plafonné."""
    if retry_after := resp.headers.get("Retry-After"):
        return min(float(retry_after), cap)
    if resp.headers.get("X-RateLimit-Remaining") == "0" and (reset := resp.headers.get("X-RateLimit-Reset")):
        return min(max(float(reset) - time.time(), 0) + 1, cap)
    return None


class Collector(ABC):
    """Interface d'un collecteur : renvoie les signaux publiés depuis `since`."""

    name: str = "abstract"

    def __init__(self, protocol: dict, session: PoliteSession):
        self.protocol = protocol
        self.session = session
        self.conf = protocol["sources"][self.name]

    @abstractmethod
    def collect(self, since: datetime) -> list[Signal]:
        ...
