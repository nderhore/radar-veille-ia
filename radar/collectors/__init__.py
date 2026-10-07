"""Registre des collecteurs. Ajouter une source = écrire une classe Collector et l'enregistrer ici."""
from radar.collectors.arxiv import ArxivCollector
from radar.collectors.base import Collector, PoliteSession
from radar.collectors.github import GitHubCollector
from radar.collectors.hackernews import HackerNewsCollector
from radar.collectors.rss import RSSCollector

REGISTRY: dict[str, type[Collector]] = {
    c.name: c for c in (ArxivCollector, HackerNewsCollector, GitHubCollector, RSSCollector)
}

# Intervalle minimal entre deux requêtes, par hôte (conditions d'utilisation des API)
RATE_LIMITS = {"export.arxiv.org": 3.0, "api.github.com": 7.0, "hn.algolia.com": 0.5}

__all__ = ["REGISTRY", "RATE_LIMITS", "Collector", "PoliteSession"]
