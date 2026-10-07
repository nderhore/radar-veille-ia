"""Collecteur RSS/Atom générique : presse spécialisée, blogs de laboratoires, régulateurs.

Analyseur volontairement minimal (bibliothèque standard) : RSS 2.0 et Atom 1.0.
Un flux en échec n'interrompt pas la collecte des autres (tolérance aux pannes).
"""
from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape

from radar.collectors.base import Collector
from radar.config import credibility, match_axis
from radar.models import Signal

log = logging.getLogger(__name__)
ATOM = "{http://www.w3.org/2005/Atom}"


class RSSCollector(Collector):
    name = "rss"

    def collect(self, since: datetime) -> list[Signal]:
        signals: list[Signal] = []
        for feed in self.conf["flux"]:
            try:
                root = ET.fromstring(self.session.get(feed["url"]).content)
            except Exception as exc:  # noqa: BLE001 : un flux défaillant est journalisé, pas bloquant
                log.warning("flux %s ignoré : %s", feed["nom"], exc)
                continue
            for item in _items(root):
                if item["published"] is None or item["published"] < since:
                    continue
                text = f"{item['title']} {item['summary']}"
                signals.append(Signal(
                    source=f"rss:{feed['nom']}",
                    source_type=feed["type"],
                    title=item["title"],
                    summary=item["summary"][:1000],
                    url=item["link"],
                    published=item["published"],
                    axis=match_axis(self.protocol, text),   # None si hors périmètre
                    credibility=credibility(self.protocol, feed["fiabilite"]),
                ))
        return signals


def _items(root: ET.Element):
    if root.tag == f"{ATOM}feed":
        for e in root.iter(f"{ATOM}entry"):
            link = e.find(f"{ATOM}link")
            yield {
                "title": _text(e.findtext(f"{ATOM}title")),
                "summary": _text(e.findtext(f"{ATOM}summary") or e.findtext(f"{ATOM}content")),
                "link": link.get("href") if link is not None else "",
                "published": _date(e.findtext(f"{ATOM}published") or e.findtext(f"{ATOM}updated")),
            }
    else:
        for e in root.iter("item"):
            yield {
                "title": _text(e.findtext("title")),
                "summary": _text(e.findtext("description")),
                "link": (e.findtext("link") or "").strip(),
                "published": _date(e.findtext("pubDate")),
            }


def _text(raw: str | None) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", unescape(raw or ""))).strip()


def _date(raw: str | None) -> datetime | None:
    if not raw:
        return None
    raw = raw.strip()
    try:
        d = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        try:
            d = parsedate_to_datetime(raw)
        except (TypeError, ValueError):
            return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
