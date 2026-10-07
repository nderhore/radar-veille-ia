"""Détection des sujets émergents : le cœur analytique du radar.

Méthode
-------
1. Deux fenêtres temporelles : récente R = ]t0 − r, t0] et référence B = ]t0 − r − b, t0 − r].
2. Termes candidats : (a) synonymes de la liste de surveillance (watchlist),
   recherchés dans les titres et résumés ; (b) n-grammes (2–3 mots) extraits
   des titres : c'est la part
   « découverte », qui permet de repérer ce que personne n'a encore nommé.
3. Pour chaque terme, test du rapport de vraisemblance G² de Dunning (1993)
   entre sa fréquence documentaire en R et en B : un G² élevé et positif
   signale une sur-représentation récente statistiquement significative.
4. Cinq indicateurs, inspirés des attributs d'une technologie émergente de
   Rotolo, Hicks & Martin (2015) : nouveauté radicale, croissance rapide,
   cohérence, impact, convergence : puis un indice composite :

       IR = Pertinence × Fiabilité × (w_m·Momentum + w_d·Diffusion + w_i·Impact + w_n·Nouveauté)
"""
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from statistics import mean
from urllib.parse import urlsplit

from radar.models import SOURCE_TYPES, Signal, Topic

STOPWORDS = set("""
a an and are as at be been being but by can could do does for from had has have how however i if in into is it its
may more most must no not of on or our over such than that the their them then there these they this those through to
under up via was we were what when where which while who why will with within without would you your also both each
other only so very new using use used based towards toward via vs versus between across among beyond show shows
le la les un une des du de et en au aux pour par sur dans avec sans est sont ce cette ces qui que quoi dont
""".split())

# Termes génériques du domaine : un n-gramme composé uniquement de ces mots n'est pas un sujet.
GENERIC = set("""
model models llm llms language large ai artificial intelligence learning machine deep neural network networks data
dataset datasets paper method methods approach approaches result results task tasks performance framework frameworks
system systems study analysis evaluation benchmark benchmarks training trained generation generative open source
tool tools application applications agent agents state art novel efficient effective via toward
""".split())

TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9\-]*[a-z0-9]|[a-z]")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def ngrams(tokens: list[str], n_min: int = 2, n_max: int = 3) -> set[str]:
    out = set()
    for n in range(n_min, n_max + 1):
        for i in range(len(tokens) - n + 1):
            gram = tokens[i:i + n]
            if gram[0] in STOPWORDS or gram[-1] in STOPWORDS or any(t in STOPWORDS for t in gram):
                continue
            if all(t in GENERIC for t in gram) or any(t.isdigit() for t in gram):
                continue
            out.add(" ".join(gram))
    return out


def g2(a: float, b: float, n_r: float, n_b: float) -> float:
    """Rapport de vraisemblance G² signé (table 2×2), Dunning (1993).

    a : documents de R contenant le terme ; b : documents de B contenant le terme ;
    n_r, n_b : effectifs totaux de R et B. Seuil usuel : 3,84 (p < 0,05) ; 10,83 (p < 0,001).
    """
    c, d = n_r - a, n_b - b
    total = n_r + n_b
    observed = (a, b, c, d)
    expected = (
        n_r * (a + b) / total, n_b * (a + b) / total,
        n_r * (c + d) / total, n_b * (c + d) / total,
    )
    stat = 2 * sum(o * math.log(o / e) for o, e in zip(observed, expected) if o > 0 and e > 0)
    return stat if (a / n_r) >= (b / n_b if n_b else 0) else -stat


def _producer(s: Signal) -> str:
    """Identité de l'émetteur, pour mesurer la cohérence (≥ 2 émetteurs indépendants)."""
    return s.authors[0].lower() if s.authors else urlsplit(s.url).netloc


def _engagement_percentiles(signals: list[Signal]) -> dict[str, float]:
    """Rang centile de l'engagement *au sein de chaque source* (les échelles ne sont pas comparables)."""
    by_source: dict[str, list[Signal]] = defaultdict(list)
    for s in signals:
        if s.engagement > 0:
            by_source[s.source].append(s)
    pct: dict[str, float] = {}
    for group in by_source.values():
        group.sort(key=lambda s: s.engagement)
        for rank, s in enumerate(group):
            pct[s.id] = (rank + 1) / len(group)
    return pct


def coverage_filter(signals: list[Signal], t_b: datetime, t_r: datetime,
                    min_share: float = 0.5) -> tuple[list[Signal], list[str]]:
    """Écarte les sources dont l'historique ne couvre pas la période de référence.

    Biais évité : un flux RSS qui n'expose que ses 20 derniers articles, ou une
    collecte plafonnée, ne présente des documents qu'en période récente : tous
    ses termes paraîtraient alors « émergents ». Une source n'est retenue que
    si son plus ancien signal remonte au moins à `min_share` de la période B.
    """
    threshold = t_r - (t_r - t_b) * min_share
    first_seen: dict[str, datetime] = {}
    for s in signals:
        if s.source not in first_seen or s.published < first_seen[s.source]:
            first_seen[s.source] = s.published
    excluded = sorted(src for src, first in first_seen.items() if first > threshold)
    return [s for s in signals if s.source not in excluded], excluded


def detect(signals: list[Signal], protocol: dict, as_of: datetime | None = None,
           feedback: dict[str, str] | None = None) -> list[Topic]:
    conf = protocol["detection"]
    feedback = feedback or {}
    t0 = as_of or max(s.published for s in signals)
    t_r = t0 - timedelta(days=conf["fenetre_recente_jours"])
    t_b = t_r - timedelta(days=conf["fenetre_reference_jours"])
    signals, _ = coverage_filter(signals, t_b, t_r)

    recent =[s for s in signals if t_r < s.published <= t0]
    baseline = [s for s in signals if t_b < s.published <= t_r]
    if not recent or not baseline:
        raise ValueError("historique insuffisant : il faut des signaux dans les deux fenêtres (R et B)")

    # --- 1. Indexation : terme -> documents --------------------------------
    watchlist = {label: (axis_id, syns) for axis_id, techs in protocol.get("watchlist", {}).items()
                 for label, syns in techs.items()}
    watch_patterns = {
        label: re.compile(r"\b(" + "|".join(re.escape(s) for s in syns) + r")\b", re.I)
        for label, (_, syns) in watchlist.items()
    }
    watch_synonyms = {syn.lower() for _, syns in watchlist.values() for syn in syns}
    watch_axis = {label.lower(): axis_id for label, (axis_id, _) in watchlist.items()}

    index: dict[str, set[str]] = defaultdict(set)   # terme -> ids
    labels: dict[str, tuple[str, str]] = {}          # terme -> (libellé, type)
    for s in recent + baseline:
        text = s.text
        for label, pat in watch_patterns.items():
            if pat.search(text):
                term = label.lower()
                index[term].add(s.id)
                labels[term] = (label, "watchlist")
        # Découverte sur les titres seulement : plus denses en termes techniques, moins bruités
        # que les résumés, et un index 10 à 20 fois plus léger.
        for gram in ngrams(tokenize(s.title)):
            if gram not in watch_synonyms:
                index[gram].add(s.id)
                labels.setdefault(gram, (gram, "discovery"))

    recent_ids = {s.id for s in recent}
    by_id = {s.id: s for s in recent + baseline}
    pct = _engagement_percentiles(recent)

    # --- 2. Statistique d'émergence et indicateurs -------------------------
    raw: list[dict] = []
    for term, ids in index.items():
        if feedback.get(term) == "bruit":
            continue
        label, kind = labels[term]
        r_ids = ids & recent_ids
        a, b = len(r_ids), len(ids) - len(r_ids)
        if a < conf["frequence_minimale"]:
            continue
        stat = g2(a, b, len(recent), len(baseline))
        ev = [by_id[i] for i in r_ids]
        if kind == "discovery":
            # Un terme inconnu doit être statistiquement significatif ET porté par ≥ 2 émetteurs.
            if stat < conf["g2_minimal"] or len({_producer(s) for s in ev}) < 2:
                continue
        types = sorted({s.source_type for s in ev})
        top_pct = sorted((pct[s.id] for s in ev if s.id in pct), reverse=True)[:5]
        axes = Counter(s.axis for s in ev if s.axis)
        raw.append({
            "term": term, "label": label, "kind": kind, "a": a, "b": b, "g2": stat,
            "diffusion": len(types) / len(SOURCE_TYPES),
            "impact": mean(top_pct) if top_pct else 0.0,
            "novelty": a / (a + b),
            "relevance": 1.0 if feedback.get(term) == "pertinent" else sum(1 for s in ev if s.axis) / a,
            "credibility": mean(s.credibility for s in ev),
            # Technologie suivie : axe déclaré dans le protocole ; terme découvert : axe majoritaire des preuves.
            "axis": watch_axis.get(term) or (axes.most_common(1)[0][0] if axes else None),
            "types": types,
            "evidence": sorted(ev, key=lambda s: (s.credibility * math.log1p(s.engagement + 1), s.published),
                               reverse=True)[: protocol["qualification"]["max_preuves_par_sujet"]],
        })
    if not raw:
        return []

    # --- 3. Normalisation du momentum et indice composite ------------------
    g2_max = max(max(r["g2"], 0) for r in raw) or 1.0
    w = conf["poids"]
    topics = []
    for r in raw:
        momentum = math.log1p(max(r["g2"], 0)) / math.log1p(g2_max)
        score = (w["momentum"] * momentum + w["diffusion"] * r["diffusion"]
                 + w["impact"] * r["impact"] + w["nouveaute"] * r["novelty"])
        topics.append(Topic(
            term=r["term"], label=r["label"], n_recent=r["a"], n_baseline=r["b"], g2=round(r["g2"], 2),
            momentum=round(momentum, 3), diffusion=round(r["diffusion"], 3), impact=round(r["impact"], 3),
            novelty=round(r["novelty"], 3), relevance=round(r["relevance"], 3),
            credibility=round(r["credibility"], 3),
            disruption_index=round(r["relevance"] * r["credibility"] * score, 4),
            axis=r["axis"], source_types=r["types"], evidence=r["evidence"], kind=r["kind"],
        ))
    topics.sort(key=lambda t: t.disruption_index, reverse=True)
    return _select(_deduplicate(topics), conf["nb_sujets_qualifies"], conf.get("part_decouverte", 0.4))


def _select(topics: list[Topic], n: int, discovery_share: float) -> list[Topic]:
    """Quota : le radar positionne les technologies suivies ET réserve des places à la découverte.

    Sans quota, l'un des deux volets évince l'autre : soit le radar ne montre que le
    connu (biais de confirmation), soit il n'affiche que des termes rares et bruités.
    Les places non pourvues par un volet sont rendues à l'autre.
    """
    discovery = [t for t in topics if t.kind == "discovery"]
    watchlist = [t for t in topics if t.kind == "watchlist"]
    n_disc = min(len(discovery), round(n * discovery_share))
    n_watch = min(len(watchlist), n - n_disc)
    n_disc = min(len(discovery), n - n_watch)
    chosen = discovery[:n_disc] + watchlist[:n_watch]
    return sorted(chosen, key=lambda t: t.disruption_index, reverse=True)


def _deduplicate(topics: list[Topic]) -> list[Topic]:
    """Élimine les n-grammes imbriqués (« speculative decoding » vs « speculative decoding method »)."""
    kept: list[Topic] = []
    for t in topics:
        words = set(t.term.split())
        if any(words <= set(k.term.split()) or set(k.term.split()) <= words for k in kept):
            continue
        kept.append(t)
    return kept
