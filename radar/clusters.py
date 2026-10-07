"""Détection d'émergence par regroupement thématique (clustering) : approche complémentaire.

La détection lexicale (detect.py) suit des *termes*. Une rupture peut pourtant
émerger sans vocabulaire stabilisé : plusieurs équipes décrivent la même idée
avec des mots différents. On regroupe donc les documents par proximité
sémantique, puis on mesure pour chaque cluster :

  * le pic de volume : G² entre période récente R et période de référence B ;
  * l'arrivée de nouveaux acteurs : part des organisations émettrices en R
    absentes de B (attractivité d'un champ, cf. théorie de la diffusion).
    Mesurée hors sources académiques : un article arXiv n'expose que des
    auteurs individuels, presque toujours « nouveaux », sans affiliation ;
  * la convergence : nombre de types de sources distincts.

Représentation : TF-IDF + réduction LSA (dépendance : scikit-learn). Pour une
représentation plus fine, remplacer `vectorize` par des embeddings
(sentence-transformers en local, ou une API d'embeddings) : le reste est inchangé.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import datetime, timedelta

from radar.detect import _producer, coverage_filter, g2
from radar.models import Signal


@dataclass
class ClusterSignal:
    cluster_id: int
    top_terms: list[str]
    n_recent: int
    n_baseline: int
    g2: float
    growth: float               # rapport des taux (lissé)
    new_entrants: float         # part des organisations récentes inédites (0 si < 5 organisations)
    source_types: list[str]
    flagged: bool               # candidat « rupture »
    examples: list[str]


def vectorize(texts: list[str], dims: int = 100):
    from sklearn.decomposition import TruncatedSVD
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.preprocessing import Normalizer

    tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=3, max_df=0.3, sublinear_tf=True)
    x = tfidf.fit_transform(texts)
    svd = TruncatedSVD(n_components=min(dims, x.shape[1] - 1), random_state=42)
    return Normalizer(copy=False).fit_transform(svd.fit_transform(x)), tfidf, x


def cluster_signals(signals: list[Signal], protocol: dict, as_of: datetime | None = None,
                    n_clusters: int | None = None) -> list[ClusterSignal]:
    import numpy as np
    from sklearn.cluster import MiniBatchKMeans

    conf = protocol["detection"]
    t0 = as_of or max(s.published for s in signals)
    t_r = t0 - timedelta(days=conf["fenetre_recente_jours"])
    t_b = t_r - timedelta(days=conf["fenetre_reference_jours"])
    signals, _ = coverage_filter(signals, t_b, t_r)
    docs = [s for s in signals if t_b < s.published <= t0]
    is_recent = np.array([s.published > t_r for s in docs])
    n_r, n_b = int(is_recent.sum()), int((~is_recent).sum())

    vectors, tfidf, x = vectorize([f"{s.title}. {s.summary[:400]}" for s in docs])
    k = n_clusters or max(8, min(60, int(math.sqrt(len(docs) / 2))))
    labels = MiniBatchKMeans(n_clusters=k, random_state=42, n_init=3, batch_size=2048).fit_predict(vectors)
    vocab = np.array(tfidf.get_feature_names_out())

    results = []
    for c in range(k):
        mask = labels == c
        a, b = int((mask & is_recent).sum()), int((mask & ~is_recent).sum())
        if a < conf["frequence_minimale"]:
            continue
        members = [docs[i] for i in np.flatnonzero(mask)]
        recent_members = [s for s in members if s.published > t_r]
        orgs = [s for s in members if s.source_type != "academic"]
        baseline_producers = {_producer(s) for s in orgs if s.published <= t_r}
        recent_producers = {_producer(s) for s in orgs if s.published > t_r}
        new_share = len(recent_producers - baseline_producers) / len(recent_producers) if len(recent_producers) >= 5 else 0.0
        stat = g2(a, b, n_r, n_b)
        growth = ((a + 0.5) / n_r) / ((b + 0.5) / n_b)
        centroid = np.asarray(x[mask].mean(axis=0)).ravel()
        results.append(ClusterSignal(
            cluster_id=c,
            top_terms=list(vocab[centroid.argsort()[::-1][:6]]),
            n_recent=a, n_baseline=b, g2=round(stat, 2), growth=round(growth, 2),
            new_entrants=round(new_share, 2),
            source_types=sorted({s.source_type for s in recent_members}),
            # Règle de signalement : pic statistiquement significatif ET croissance ≥ ×2,
            # ou champ massivement investi par de nouveaux acteurs.
            flagged=(stat >= conf["g2_minimal"] and growth >= 2) or (new_share >= 0.8 and growth >= 1.5),
            examples=[s.title for s in sorted(recent_members, key=lambda s: -s.engagement)[:3]],
        ))
    results.sort(key=lambda r: (not r.flagged, -r.g2))
    return results


def clusters_markdown(results: list[ClusterSignal]) -> str:
    lines = ["# Clusters thématiques : pics de volume et nouveaux entrants", "",
             "| Cluster | Termes caractéristiques | R | B | G² | Croissance | Nouveaux acteurs | Sources | Signal |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r.cluster_id} | {', '.join(r.top_terms)} | {r.n_recent} | {r.n_baseline} | {r.g2} | "
                     f"×{r.growth} | {r.new_entrants:.0%} | {', '.join(r.source_types)} | "
                     f"{'**rupture ?**' if r.flagged else ''} |")
    lines += ["", "## Exemples (clusters signalés)", ""]
    for r in (r for r in results if r.flagged):
        lines.append(f"**Cluster {r.cluster_id}** ({', '.join(r.top_terms[:3])})")
        lines += [f"- {t}" for t in r.examples] + [""]
    return "\n".join(lines)
