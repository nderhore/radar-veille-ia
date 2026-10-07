"""Modèle de données du radar : le *signal*, unité élémentaire de la veille.

Un signal est une observation datée, sourcée et cotée. Toute la chaîne
(collecte, stockage, détection, qualification, restitution) manipule
des signaux ; les sujets (Topic) en sont des agrégats.
"""
from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from urllib.parse import urlsplit, urlunsplit

SOURCE_TYPES = ("academic", "code", "community", "press", "regulatory")


def canonical_url(url: str) -> str:
    """Normalise une URL (schéma, casse de l'hôte, slash final, fragments, query de tracking)."""
    parts = urlsplit(url.strip())
    query = "&".join(
        p for p in parts.query.split("&") if p and not p.lower().startswith(("utm_", "ref=", "fbclid"))
    )
    path = parts.path.rstrip("/") or "/"
    return urlunsplit(("https", parts.netloc.lower().removeprefix("www."), path, query, ""))


@dataclass
class Signal:
    source: str                 # collecteur : arxiv, hackernews, github, rss:<nom>
    source_type: str            # typologie, cf. SOURCE_TYPES
    title: str
    url: str
    published: datetime         # toujours en UTC
    summary: str = ""
    authors: list[str] = field(default_factory=list)
    axis: str | None = None     # KIT de rattachement (None si non rattaché)
    engagement: float = 0.0     # étoiles, points, commentaires… (brut, propre à la source)
    credibility: float = 0.5    # fiabilité de la source, [0, 1]
    id: str = ""

    def __post_init__(self) -> None:
        if self.source_type not in SOURCE_TYPES:
            raise ValueError(f"source_type inconnu : {self.source_type!r}")
        if self.published.tzinfo is None:
            self.published = self.published.replace(tzinfo=timezone.utc)
        if not self.id:
            # Dédoublonnage *intra-source* uniquement : un même article présent sur
            # arXiv ET sur Hacker News constitue deux signaux distincts, car la
            # convergence inter-sources est elle-même un indicateur de diffusion.
            key = f"{self.source}|{canonical_url(self.url)}"
            self.id = hashlib.sha1(key.encode()).hexdigest()[:16]

    @property
    def text(self) -> str:
        return f"{self.title}. {self.summary}"

    def to_dict(self) -> dict:
        d = asdict(self)
        d["published"] = self.published.isoformat()
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Signal":
        d = dict(d)
        d["published"] = datetime.fromisoformat(d["published"])
        return cls(**d)


@dataclass
class Topic:
    """Sujet candidat issu de la détection : un terme et ses indicateurs d'émergence."""
    term: str
    label: str
    n_recent: int
    n_baseline: int
    g2: float                   # log-likelihood ratio signé (Dunning, 1993)
    momentum: float             # [0, 1] après normalisation
    diffusion: float            # [0, 1] nb de types de sources distincts / 5
    impact: float               # [0, 1] engagement percentile moyen
    novelty: float              # [0, 1] n_recent / (n_recent + n_baseline)
    relevance: float            # [0, 1] part des preuves rattachées à un axe
    credibility: float          # [0, 1] fiabilité moyenne des preuves
    disruption_index: float     # indice composite final
    axis: str | None
    source_types: list[str]
    evidence: list[Signal] = field(default_factory=list)
    kind: str = "discovery"     # watchlist (technologie suivie) | discovery (terme émergent inconnu)


@dataclass
class RadarEntry:
    """Sujet qualifié, positionné sur le radar."""
    label: str
    quadrant: str
    ring: str
    trl: int                    # Technology Readiness Level estimé (1–9)
    innovation_type: str        # incrementale | radicale | rupture
    impact: int                 # 1–5
    confidence: int             # 1–5
    rationale: str
    action: str
    kiq: list[str]
    disruption_index: float
    evidence_urls: list[str]
    moved: str = "new"          # new | in | out | stable (vs. radar précédent)
