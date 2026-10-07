"""Collecteur GitHub (API Search) : signal d'adoption par les développeurs.

API : https://docs.github.com/rest/search. Sans jeton : 10 requêtes/min ;
avec la variable d'environnement GITHUB_TOKEN : 30 requêtes/min.
Position dans le cycle de vie : implémentations ouvertes (TRL 4–6).
"""
from __future__ import annotations

import os
from datetime import datetime

from radar.collectors.base import Collector
from radar.config import credibility, match_axis
from radar.models import Signal

API = "https://api.github.com/search/repositories"


class GitHubCollector(Collector):
    name = "github"

    def collect(self, since: datetime) -> list[Signal]:
        headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if token := os.environ.get("GITHUB_TOKEN"):
            headers["Authorization"] = f"Bearer {token}"
        signals: dict[str, Signal] = {}
        for axis in self.protocol["axes"]:
            for query in axis["requetes"]["github"]:
                q = f"{query} created:>={since:%Y-%m-%d} stars:>={self.conf['etoiles_minimum']}"
                params = {"q": q, "sort": "stars", "order": "desc", "per_page": self.conf["max_resultats_par_requete"]}
                for repo in self.session.get(API, params=params, headers=headers).json().get("items", []):
                    text = f"{repo['full_name']} {repo.get('description') or ''} {' '.join(repo.get('topics', []))}"
                    s = Signal(
                        source=self.name,
                        source_type=self.conf["type"],
                        title=repo["full_name"] + (f" : {repo['description']}" if repo.get("description") else ""),
                        summary=" ".join(repo.get("topics", [])),
                        url=repo["html_url"],
                        published=datetime.fromisoformat(repo["created_at"].replace("Z", "+00:00")),
                        authors=[repo["owner"]["login"]],
                        axis=match_axis(self.protocol, text) or axis["id"],
                        engagement=float(repo["stargazers_count"]),
                        credibility=credibility(self.protocol, self.conf["fiabilite"]),
                    )
                    signals[s.id] = s
        return list(signals.values())
