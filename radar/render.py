"""Restitution : radar visuel (HTML/SVG autonome), note de veille (Markdown), export JSON.

Le livrable est pensé pour ses destinataires : le radar pour la vision
d'ensemble (CODIR), la note de veille pour la décision argumentée, le JSON pour
l'intégration dans d'autres outils (tableau de bord, base de connaissances).
"""
from __future__ import annotations

import json
import math
import random
import re
from dataclasses import asdict
from html import escape
from pathlib import Path

from radar.models import RadarEntry

SIZE = 760
CENTER = SIZE / 2
RING_RADII = [100, 190, 270, 340]
QUADRANT_COLORS = ["#2f6fdf", "#1a9e75", "#d9822b", "#b84a9e"]
MOVE_LABELS = {"new": "nouveau", "in": "rapproché du centre", "out": "éloigné du centre", "stable": "stable"}
TYPE_LABELS = {"incrementale": "incrémentale", "radicale": "radicale", "rupture": "rupture"}


def _place(entries: list[RadarEntry], protocol: dict) -> list[tuple[RadarEntry, float, float]]:
    """Position déterministe (graine = libellé) avec évitement des collisions."""
    quadrants = [a["quadrant"] for a in protocol["axes"]]
    rings = [r["id"] for r in protocol["anneaux"]]
    placed: list[tuple[RadarEntry, float, float]] = []
    for e in sorted(entries, key=lambda e: -e.disruption_index):
        q, r = quadrants.index(e.quadrant), rings.index(e.ring)
        r_in, r_out = (RING_RADII[r - 1] if r else 0) + 14, RING_RADII[r] - 14
        rng = random.Random(e.label)
        best = None
        for _ in range(60):
            angle = math.radians(q * 90 + 8 + rng.random() * 74)
            radius = r_in + rng.random() * max(r_out - r_in, 1)
            x, y = CENTER + radius * math.cos(angle), CENTER - radius * math.sin(angle)
            gap = min((math.dist((x, y), (px, py)) for _, px, py in placed), default=99)
            if best is None or gap > best[0]:
                best = (gap, x, y)
            if gap >= 24:
                break
        placed.append((e, best[1], best[2]))
    return placed


def radar_svg(entries: list[RadarEntry], protocol: dict) -> tuple[str, list[tuple[int, RadarEntry]]]:
    quadrants = [a["quadrant"] for a in protocol["axes"]]
    parts = [f'<svg viewBox="0 0 {SIZE} {SIZE}" role="img" aria-label="Radar d\'innovation" '
             f'xmlns="http://www.w3.org/2000/svg" font-family="inherit">']
    for radius, ring in reversed(list(zip(RING_RADII, protocol["anneaux"]))):
        parts.append(f'<circle cx="{CENTER}" cy="{CENTER}" r="{radius}" fill="var(--ring)" stroke="var(--line)"/>')
        parts.append(f'<text x="{CENTER + 4}" y="{CENTER - radius + 14}" font-size="11" fill="var(--muted)">'
                     f'{escape(ring["libelle"])}</text>')
    parts.append(f'<line x1="{CENTER}" y1="0" x2="{CENTER}" y2="{SIZE}" stroke="var(--line)"/>')
    parts.append(f'<line x1="0" y1="{CENTER}" x2="{SIZE}" y2="{CENTER}" stroke="var(--line)"/>')
    corners = [(SIZE - 8, 18, "end"), (8, 18, "start"), (8, SIZE - 8, "start"), (SIZE - 8, SIZE - 8, "end")]
    for (x, y, anchor), name, color in zip(corners, quadrants, QUADRANT_COLORS):
        parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="14" font-weight="600" '
                     f'fill="{color}">{escape(name)}</text>')

    numbered = []
    placed = _place(entries, protocol)
    placed.sort(key=lambda p: (quadrants.index(p[0].quadrant), -p[0].disruption_index))
    for n, (e, x, y) in enumerate(placed, start=1):
        color = QUADRANT_COLORS[quadrants.index(e.quadrant)]
        title = f"<title>{n}. {escape(e.label)} : {escape(MOVE_LABELS[e.moved])}</title>"
        if e.moved == "in":
            shape = f'<path d="M{x},{y - 11} L{x + 10},{y + 7} L{x - 10},{y + 7} Z" fill="{color}"/>'
        elif e.moved == "out":
            shape = f'<path d="M{x},{y + 11} L{x + 10},{y - 7} L{x - 10},{y - 7} Z" fill="{color}"/>'
        elif e.moved == "new":
            shape = (f'<circle cx="{x}" cy="{y}" r="12" fill="none" stroke="{color}" stroke-width="2"/>'
                     f'<circle cx="{x}" cy="{y}" r="8.5" fill="{color}"/>')
        else:
            shape = f'<circle cx="{x}" cy="{y}" r="9" fill="{color}"/>'
        parts.append(f'<g>{title}{shape}<text x="{x}" y="{y + 3.5}" text-anchor="middle" font-size="9.5" '
                     f'font-weight="700" fill="#fff">{n}</text></g>')
        numbered.append((n, e))
    parts.append("</svg>")
    return "\n".join(parts), numbered


def radar_html(entries: list[RadarEntry], protocol: dict, meta: dict) -> str:
    svg, numbered = radar_svg(entries, protocol)
    rings = {r["id"]: r for r in protocol["anneaux"]}
    rows = "\n".join(
        f"<tr><td>{n}</td><td><a href='#e{n}'>{escape(e.label)}</a></td><td>{escape(e.quadrant)}</td>"
        f"<td>{escape(rings[e.ring]['libelle'])}</td><td>{e.trl}</td><td>{TYPE_LABELS[e.innovation_type]}</td>"
        f"<td>{e.impact}/5</td><td>{e.confidence}/5</td><td>{e.disruption_index:.3f}</td>"
        f"<td>{MOVE_LABELS[e.moved]}</td></tr>"
        for n, e in numbered
    )
    cards = "\n".join(
        f"<article id='e{n}'><h3>{n}. {escape(e.label)}</h3>"
        f"<p class='tags'>{escape(e.quadrant)} · {escape(rings[e.ring]['libelle'])} ({escape(rings[e.ring]['horizon'])})"
        f" · TRL {e.trl} · {TYPE_LABELS[e.innovation_type]}</p>"
        f"<p><strong>Analyse.</strong> {escape(e.rationale)}</p>"
        f"<p><strong>Action recommandée.</strong> {escape(e.action)}</p>"
        + (f"<p><strong>KIQ.</strong> {escape(', '.join(e.kiq))}</p>" if e.kiq else "")
        + "<details><summary>Preuves</summary><ul>"
        + "".join(f"<li><a href='{escape(u)}' rel='noopener noreferrer'>{escape(u)}</a></li>" for u in e.evidence_urls)
        + "</ul></details></article>"
        for n, e in numbered
    )
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Radar d'innovation IA</title>
<style>
:root {{ --bg:#fbfaf7; --fg:#1d1d1f; --muted:#6b6b70; --line:#d9d6cf; --ring:rgba(0,0,0,.025); --card:#fff; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#16171a; --fg:#ececec; --muted:#9a9aa0; --line:#34353a;
  --ring:rgba(255,255,255,.03); --card:#1f2024; }} }}
body {{ margin:0; background:var(--bg); color:var(--fg); font:15px/1.55 system-ui, -apple-system, sans-serif; }}
main {{ max-width:1100px; margin:0 auto; padding:24px 16px 64px; }}
h1 {{ font-size:1.6rem; margin:0 0 4px; }} .meta {{ color:var(--muted); font-size:.9rem; }}
svg {{ width:100%; max-width:760px; display:block; margin:24px auto; }}
table {{ width:100%; border-collapse:collapse; font-size:.88rem; }} .scroll {{ overflow-x:auto; }}
th, td {{ text-align:left; padding:6px 8px; border-bottom:1px solid var(--line); white-space:nowrap; }}
article {{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:4px 18px; margin:14px 0; }}
.tags {{ color:var(--muted); font-size:.88rem; }} a {{ color:inherit; }}
</style></head><body><main>
<h1>Radar d'innovation : Intelligence artificielle</h1>
<p class="meta">Arrêté au {escape(meta['as_of'])} · Protocole v{escape(meta['protocol_version'])} ·
Qualification : {escape(meta['method'])} · {meta['n_recent']} signaux récents / {meta['n_baseline']} de référence</p>
{svg}
<p class="meta">Livrables : <a href="note-de-veille.html">note de veille</a> · <a href="radar.json">données JSON</a> ·
<a href="radar-zalando.json">format Zalando Tech Radar</a> · <a href="radar-byor.csv">format Build your own Radar (CSV)</a></p>
<p class="meta">Forme des points : cercle cerclé = nouveau ; triangle pointe en haut = rapproché du centre ;
pointe en bas = éloigné ; cercle plein = inchangé.</p>
<h2>Synthèse</h2>
<div class="scroll"><table><thead><tr><th>#</th><th>Sujet</th>
<th title="Axe de surveillance (KIT) auquel le sujet se rattache">Quadrant</th>
<th title="Horizon de décision, et non note de qualité">Anneau</th>
<th title="Maturité technologique de 1 à 9 (ISO 16290), estimée d'après les types de sources">TRL</th>
<th title="Incrémentale, radicale ou rupture">Type</th>
<th title="Écho chez les praticiens : engagement (étoiles, points)">Impact</th>
<th title="Solidité du constat : diversité des types de sources">Confiance</th>
<th title="Indice de rupture entre 0 et 1, pour trier les sujets d'un même radar">Indice</th>
<th title="Évolution de l'anneau depuis le radar précédent">Mouvement</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="meta">Survoler un en-tête de colonne pour sa définition ; la légende complète figure dans la
<a href="note-de-veille.html">note de veille</a>.</p>
<h2>Fiches</h2>
{cards}
</main></body></html>"""


def note_markdown(entries: list[RadarEntry], protocol: dict, meta: dict) -> str:
    rings = {r["id"]: r for r in protocol["anneaux"]}
    order = [r["id"] for r in protocol["anneaux"]]
    ranked = sorted(entries, key=lambda e: (order.index(e.ring), -e.impact, -e.disruption_index))
    lines = [
        f"# Note de veille du radar d'innovation IA (arrêté au {meta['as_of']})",
        "",
        "| Rubrique | Valeur |",
        "|---|---|",
        f"| Émetteur | {protocol['meta']['owner']} |",
        f"| Destinataires | {', '.join(protocol['diffusion']['destinataires'])} |",
        f"| Version du protocole | {protocol['meta']['version']} |",
        f"| Méthode de qualification | {meta['method']} |",
        f"| Corpus | {meta['n_recent']} signaux récents, {meta['n_baseline']} signaux de référence |",
        "| Classification | Diffusion restreinte (interne) |",
        "",
        "## 1. Synthèse exécutive",
        "",
    ]
    for e in ranked[:3]:
        lines.append(f"- **{e.label}** ({rings[e.ring]['libelle']}, {rings[e.ring]['horizon']}) : {e.action}")
    lines += ["", "## 2. Mouvements depuis le radar précédent", ""]
    for code, title in (("new", "Entrées nouvelles"), ("in", "Rapprochements du centre"), ("out", "Éloignements")):
        items = [e.label for e in entries if e.moved == code]
        lines.append(f"- {title} : {', '.join(items) if items else 'aucun'}")
    lines += ["", "## 3. Tableau du radar", "",
              "| Sujet | Quadrant | Anneau | TRL | Type | Impact | Confiance | Indice | Mouvement |",
              "|---|---|---|---|---|---|---|---|---|"]
    for e in ranked:
        lines.append(f"| {e.label} | {e.quadrant} | {rings[e.ring]['libelle']} | {e.trl} | "
                     f"{TYPE_LABELS[e.innovation_type]} | {e.impact}/5 | {e.confidence}/5 | {e.disruption_index:.3f} | "
                     f"{MOVE_LABELS[e.moved]} |")
    horizons = ", ".join(f"{r['libelle']} {r['horizon']}" for r in protocol["anneaux"])
    lines += ["", "Lecture des colonnes :", "",
              "- **Quadrant** : axe de surveillance (KIT) auquel le sujet se rattache.",
              f"- **Anneau** : horizon de décision ({horizons}), et non note de qualité.",
              "- **TRL** : maturité technologique de 1 à 9 (ISO 16290), estimée d'après les types de sources.",
              "- **Type** : incrémentale (améliore l'existant), radicale (approche nouvelle), rupture (modifie le marché).",
              "- **Impact** : écho chez les praticiens, mesuré par l'engagement (étoiles, points).",
              "- **Confiance** : solidité du constat, croissante avec la diversité des types de sources.",
              "- **Indice** : indice de rupture entre 0 et 1, qui sert à trier les sujets d'un même radar.",
              "- **Mouvement** : évolution de l'anneau depuis le radar précédent."]
    lines += ["", "## 4. Fiches d'analyse", ""]
    for e in ranked:
        lines += [f"### {e.label}", "",
                  f"*{e.quadrant}, {rings[e.ring]['libelle']} ({rings[e.ring]['horizon']}), TRL {e.trl}*", "",
                  f"**Analyse.** {e.rationale}", "", f"**Action recommandée.** {e.action}", ""]
        if e.kiq:
            lines += [f"**KIQ adressées.** {', '.join(e.kiq)}", ""]
        lines += ["**Preuves.**", *[f"- <{u}>" for u in e.evidence_urls[:5]], ""]
    det = protocol["detection"]
    lines += [
        "## 5. Méthodologie et limites", "",
        f"- Fenêtre récente : {det['fenetre_recente_jours']} jours ; fenêtre de référence : "
        f"{det['fenetre_reference_jours']} jours.",
        f"- Seuils : fréquence ≥ {det['frequence_minimale']} documents, G² ≥ {det['g2_minimal']} (sujets découverts).",
        "- Indice de rupture = Pertinence × Fiabilité × Σ(poids × indicateur) ; poids : "
        + ", ".join(f"{k} {v}" for k, v in det["poids"].items()) + ".",
        "- Limites : biais de couverture des sources (anglophones, ouvertes) ; la qualification automatique "
        "est une proposition soumise à validation humaine ; l'engagement communautaire peut être manipulé.",
        "",
    ]
    return "\n".join(lines)


def zalando_json(entries: list[RadarEntry], protocol: dict, meta: dict) -> dict:
    """Format d'entrée du Zalando Tech Radar (github.com/zalando/tech-radar)."""
    quadrants = [a["quadrant"] for a in protocol["axes"]]
    rings = [r["id"] for r in protocol["anneaux"]]
    # Zalando ordonne les quadrants : 0 bas-droite, 1 bas-gauche, 2 haut-gauche, 3 haut-droite.
    zalando_quadrant = {0: 3, 1: 2, 2: 1, 3: 0}
    moved = {"stable": 0, "in": 1, "out": -1, "new": 2}
    return {
        "date": meta["as_of"],
        "quadrants": [{"name": quadrants[i]} for i in (3, 2, 1, 0)],
        "rings": [{"name": r["libelle"]} for r in protocol["anneaux"]],
        "entries": [{"label": e.label, "quadrant": zalando_quadrant[quadrants.index(e.quadrant)],
                     "ring": rings.index(e.ring), "moved": moved[e.moved], "active": True,
                     "link": e.evidence_urls[0] if e.evidence_urls else ""} for e in entries],
    }


def byor_csv(entries: list[RadarEntry], protocol: dict) -> str:
    """CSV pour Thoughtworks « Build your own Radar » (colonnes name, ring, quadrant, isNew, description)."""
    import csv
    import io

    rings = {r["id"]: r["libelle"] for r in protocol["anneaux"]}
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["name", "ring", "quadrant", "isNew", "description"])
    for e in entries:
        writer.writerow([e.label, rings[e.ring], e.quadrant, str(e.moved == "new").upper(),
                         f"{e.rationale} Action : {e.action}"])
    return buf.getvalue()


def note_html(markdown: str) -> str:
    """Conversion minimale de la note de veille en HTML (titres, tableaux, listes, gras, italique, liens)."""
    def inline(t: str) -> str:
        t = escape(t, quote=False)
        t = re.sub(r"&lt;(https?://[^&]+)&gt;", r'<a href="\1" rel="noopener noreferrer">\1</a>', t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        return re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)

    html, in_list, in_table = [], False, False
    for line in markdown.splitlines():
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if set("".join(cells)) <= set("-: "):
                continue
            tag = "th" if not in_table else "td"
            if not in_table:
                html.append("<table>")
                in_table = True
            html.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
            continue
        if in_table:
            html.append("</table>")
            in_table = False
        if line.startswith("- "):
            if not in_list:
                html.append("<ul>")
                in_list = True
            html.append(f"<li>{inline(line[2:])}</li>")
            continue
        if in_list:
            html.append("</ul>")
            in_list = False
        m = re.match(r"(#{1,3}) (.*)", line)
        if m:
            level = len(m.group(1))
            html.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        elif line.strip():
            html.append(f"<p>{inline(line)}</p>")
    if in_table:
        html.append("</table>")
    if in_list:
        html.append("</ul>")
    return f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Note de veille</title>
<style>
:root {{ --bg:#fbfaf7; --fg:#1d1d1f; --muted:#6b6b70; --line:#d9d6cf; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#16171a; --fg:#ececec; --muted:#9a9aa0; --line:#34353a; }} }}
body {{ margin:0; background:var(--bg); color:var(--fg); font:15px/1.6 system-ui, -apple-system, sans-serif; }}
main {{ max-width:960px; margin:0 auto; padding:24px 16px 64px; }}
table {{ border-collapse:collapse; width:100%; font-size:.9rem; display:block; overflow-x:auto; }}
th, td {{ text-align:left; padding:6px 8px; border-bottom:1px solid var(--line); }}
a {{ color:inherit; }} h1 {{ font-size:1.6rem; }}
</style></head><body><main>
<p><a href="index.html">Retour au radar</a></p>
{chr(10).join(html)}
</main></body></html>"""


def write_outputs(entries: list[RadarEntry], protocol: dict, meta: dict, out_dir: str | Path) -> dict[str, Path]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    paths = {"html": out / "radar.html", "note": out / "note-de-veille.md", "note_html": out / "note-de-veille.html",
             "json": out / "radar.json",
             "zalando": out / "radar-zalando.json", "byor": out / "radar-byor.csv"}
    paths["html"].write_text(radar_html(entries, protocol, meta), encoding="utf-8")
    note = note_markdown(entries, protocol, meta)
    paths["note"].write_text(note, encoding="utf-8")
    paths["note_html"].write_text(note_html(note), encoding="utf-8")
    paths["json"].write_text(json.dumps({"meta": meta, "entries": [asdict(e) for e in entries]},
                                        ensure_ascii=False, indent=2), encoding="utf-8")
    paths["zalando"].write_text(json.dumps(zalando_json(entries, protocol, meta), ensure_ascii=False, indent=2),
                                encoding="utf-8")
    paths["byor"].write_text(byor_csv(entries, protocol), encoding="utf-8")
    return paths
