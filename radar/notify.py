"""Diffusion « push » : alerte synthétique vers un canal d'équipe (Slack, Teams, Mattermost).

Seuls les mouvements significatifs sont poussés (nouveaux sujets en « Agir » ou
« Préparer », rapprochements du centre) : une alerte trop fréquente n'est plus lue.
"""
from __future__ import annotations

import os

import requests

from radar.models import RadarEntry


def build_alert(entries: list[RadarEntry], protocol: dict, report_url: str = "") -> str | None:
    rings = {r["id"]: r["libelle"] for r in protocol["anneaux"]}
    notable = [e for e in entries
               if e.moved == "in" or (e.moved == "new" and e.ring in ("agir", "preparer"))]
    if not notable:
        return None
    lines = ["*Radar IA : mouvements significatifs*"]
    lines += [f"- {e.label} : {rings[e.ring]} (TRL {e.trl}, impact {e.impact}/5) : {e.action}" for e in notable]
    if report_url:
        lines.append(f"Note complète : {report_url}")
    return "\n".join(lines)


def send(text: str, protocol: dict) -> bool:
    url = os.environ.get(protocol["diffusion"]["webhook_env"])
    if not url:
        return False
    # Format « text » accepté par les webhooks entrants Slack et Mattermost (Teams : adapter la charge utile).
    requests.post(url, json={"text": text}, timeout=15).raise_for_status()
    return True
