"""Collecteur arXiv : signal académique (pré-publications).

API : https://info.arxiv.org/help/api/user-manual.html (Atom 1.0, 1 requête / 3 s).
Position dans le cycle de vie d'une technologie : très amont (TRL 1–3).

Le volume quotidien d'arXiv en IA étant élevé, la collecte est paginée jusqu'à
couvrir toute la profondeur d'historique demandée (ou jusqu'au plafond fixé
par le protocole, auquel cas la couverture sera signalée comme incomplète).
"""
from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from datetime import datetime

from radar.collectors.base import Collector
from radar.config import credibility
from radar.models import Signal

log = logging.getLogger(__name__)
API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom"}
PAGE_SIZE = 500


class ArxivCollector(Collector):
    name = "arxiv"

    def collect(self, since: datetime) -> list[Signal]:
        signals: list[Signal] = []
        cap = self.conf["max_resultats_par_axe"]
        for axis in self.protocol["axes"]:
            start, reached_since = 0, False
            while start < cap and not reached_since:
                params = {
                    "search_query": axis["requetes"]["arxiv"],
                    "sortBy": "submittedDate",
                    "sortOrder": "descending",
                    "start": start,
                    "max_results": min(PAGE_SIZE, cap - start),
                }
                entries = ET.fromstring(self.session.get(API, params=params).content).findall("a:entry", NS)
                if not entries:
                    break
                for entry in entries:
                    published = datetime.fromisoformat(
                        entry.findtext("a:published", namespaces=NS).replace("Z", "+00:00"))
                    if published < since:
                        reached_since = True   # résultats triés par date décroissante
                        break
                    signals.append(self._to_signal(entry, published, axis["id"]))
                start += len(entries)
            if not reached_since:
                log.warning("arXiv %s : plafond de %d résultats atteint avant le %s (couverture partielle)",
                            axis["id"], cap, since.date())
        return signals

    def _to_signal(self, entry: ET.Element, published: datetime, axis_id: str) -> Signal:
        return Signal(
            source=self.name,
            source_type=self.conf["type"],
            title=_clean(entry.findtext("a:title", namespaces=NS)),
            summary=_clean(entry.findtext("a:summary", namespaces=NS)),
            url=entry.findtext("a:id", namespaces=NS),
            published=published,
            authors=[a.findtext("a:name", namespaces=NS) for a in entry.findall("a:author", NS)][:10],
            axis=axis_id,
            credibility=credibility(self.protocol, self.conf["fiabilite"]),
        )


def _clean(text: str | None) -> str:
    return re.sub(r"\s+", " ", text or "").strip()
