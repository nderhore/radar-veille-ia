"""Chargement et validation du protocole de veille (config/protocole.yaml)."""
from __future__ import annotations

import math
from pathlib import Path

import yaml

DEFAULT_PATH = Path(__file__).resolve().parent.parent / "config" / "protocole.yaml"


class ProtocolError(ValueError):
    pass


def load_protocol(path: str | Path = DEFAULT_PATH) -> dict:
    with open(path, encoding="utf-8") as f:
        protocol = yaml.safe_load(f)
    validate(protocol)
    return protocol


def validate(p: dict) -> None:
    """Contrôles de cohérence : un protocole invalide ne doit jamais tourner en production."""
    for key in ("meta", "axes", "sources", "detection", "anneaux"):
        if key not in p:
            raise ProtocolError(f"section obligatoire absente : {key}")

    ids = [a["id"] for a in p["axes"]]
    if len(ids) != len(set(ids)):
        raise ProtocolError("identifiants d'axes (KIT) dupliqués")
    if len(p["axes"]) != 4:
        raise ProtocolError("le radar attend exactement 4 axes (un par quadrant)")

    weights = p["detection"]["poids"]
    if not math.isclose(sum(weights.values()), 1.0, abs_tol=1e-6):
        raise ProtocolError(f"les poids de l'indice de rupture doivent sommer à 1 (actuel : {sum(weights.values())})")

    if p["detection"]["fenetre_recente_jours"] >= p["detection"]["fenetre_reference_jours"]:
        raise ProtocolError("la fenêtre de référence doit être plus longue que la fenêtre récente")

    unknown = set(p.get("watchlist", {})) - set(ids)
    if unknown:
        raise ProtocolError(f"watchlist rattachée à des axes inconnus : {sorted(unknown)}")

    grades = p["cotation_fiabilite"]
    for name, src in p["sources"].items():
        if name == "rss":
            for feed in src.get("flux", []):
                if feed["fiabilite"] not in grades:
                    raise ProtocolError(f"cotation inconnue pour le flux {feed['nom']}")
        elif src["fiabilite"] not in grades:
            raise ProtocolError(f"cotation inconnue pour la source {name}")


def credibility(p: dict, grade: str) -> float:
    return float(p["cotation_fiabilite"][grade])


def axis_by_id(p: dict, axis_id: str | None) -> dict | None:
    return next((a for a in p["axes"] if a["id"] == axis_id), None)


def match_axis(p: dict, text: str) -> str | None:
    """Rattache un texte à l'axe dont il contient le plus de mots-clés (None si aucun)."""
    text = text.lower()
    scores = {a["id"]: sum(kw in text for kw in a["mots_cles"]) for a in p["axes"]}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else None
