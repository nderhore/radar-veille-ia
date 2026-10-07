"""Collecteur Hacker News (API Algolia) : signal communautaire.

API : https://hn.algolia.com/api (sans clé). Signal précoce mais bruité :
l'engagement (points) sert de filtre minimal et d'indicateur d'impact.
"""
from __future__ import annotations

from datetime import datetime, timezone

from radar.collectors.base import Collector
from radar.config import credibility, match_axis
from radar.models import Signal

API = "https://hn.algolia.com/api/v1/search_by_date"


class HackerNewsCollector(Collector):
    name = "hackernews"

    def collect(self, since: datetime) -> list[Signal]:
        signals: dict[str, Signal] = {}
        for axis in self.protocol["axes"]:
            for query in axis["requetes"]["hackernews"]:
                params = {
                    "query": query,
                    "tags": "story",
                    "numericFilters": f"created_at_i>{int(since.timestamp())},points>={self.conf['points_minimum']}",
                    "hitsPerPage": self.conf["max_resultats_par_requete"],
                }
                for hit in self.session.get(API, params=params).json()["hits"]:
                    title = hit.get("title") or ""
                    s = Signal(
                        source=self.name,
                        source_type=self.conf["type"],
                        title=title,
                        url=hit.get("url") or f"https://news.ycombinator.com/item?id={hit['objectID']}",
                        published=datetime.fromtimestamp(hit["created_at_i"], tz=timezone.utc),
                        # La requête a pu remonter un document hors sujet : on rattache
                        # par mots-clés, et à défaut à l'axe de la requête.
                        axis=match_axis(self.protocol, title) or axis["id"],
                        engagement=float(hit.get("points") or 0) + 0.5 * float(hit.get("num_comments") or 0),
                        credibility=credibility(self.protocol, self.conf["fiabilite"]),
                    )
                    signals[s.id] = s   # dédoublonnage entre requêtes
        return list(signals.values())
