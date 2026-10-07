"""Interface en ligne de commande : orchestration du cycle de veille.

    python -m radar collect              # collecte (sources du protocole) : SQLite
    python -m radar analyze              # détection, qualification, restitution
    python -m radar run                  # collect + analyze (exécution planifiée)
    python -m radar demo                 # rejoue le jeu de données figé (sans réseau)
    python -m radar clusters             # émergence par clustering thématique (scikit-learn)
    python -m radar feedback TERME bruit # retour analyste (boucle de rétroaction)
    python -m radar stats                # indicateurs de pilotage du dispositif
"""
from __future__ import annotations

import argparse
import gzip
import json
import logging
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from radar.collectors import RATE_LIMITS, REGISTRY, PoliteSession
from radar.config import DEFAULT_PATH, load_protocol
from radar.detect import detect
from radar.models import Signal
from radar.notify import build_alert, send
from radar.qualify import compute_moves, qualify
from radar.render import write_outputs
from radar.store import Store

log = logging.getLogger("radar")
ROOT = Path(__file__).resolve().parent.parent
SAMPLE = ROOT / "samples" / "signals_demo.jsonl.gz"


def cmd_collect(args, protocol: dict, store: Store) -> int:
    det = protocol["detection"]
    lookback = det["fenetre_recente_jours"] + det["fenetre_reference_jours"]
    # Collecte incrémentale : on repart du dernier signal connu (avec recouvrement de 2 jours).
    latest = store.latest_published()
    since = (latest - timedelta(days=2)) if latest and not args.full else \
        datetime.now(timezone.utc) - timedelta(days=lookback)
    session = PoliteSession(min_interval=RATE_LIMITS)
    collected, errors = [], []
    for name, cls in REGISTRY.items():
        if not protocol["sources"].get(name, {}).get("actif"):
            continue
        try:
            batch = cls(protocol, session).collect(since)
            log.info("%-11s %4d signaux", name, len(batch))
            collected += batch
        except Exception as exc:  # noqa: BLE001 : une source en échec ne doit pas bloquer le cycle
            log.error("collecteur %s en échec : %s", name, exc)
            errors.append(f"{name}: {exc}")
    inserted = store.upsert_signals(collected)
    store.log_run(datetime.now(timezone.utc), len(collected), inserted, errors)
    log.info("collecte terminée : %d signaux reçus, %d nouveaux, %d en base", len(collected), inserted, store.count())
    if args.export:
        with open(args.export, "w", encoding="utf-8") as f:
            for s in store.signals_since(since):
                f.write(json.dumps(s.to_dict(), ensure_ascii=False) + "\n")
    return 1 if errors and not collected else 0


def cmd_analyze(args, protocol: dict, store: Store) -> int:
    det = protocol["detection"]
    as_of = datetime.fromisoformat(args.as_of).replace(tzinfo=timezone.utc) if args.as_of else store.latest_published()
    if as_of is None:
        log.error("base vide : lancer d'abord `collect` ou `demo`")
        return 1
    window_start = as_of - timedelta(days=det["fenetre_recente_jours"] + det["fenetre_reference_jours"])
    signals = [s for s in store.signals_since(window_start) if s.published <= as_of]

    topics = detect(signals, protocol, as_of=as_of, feedback=store.feedback())
    log.info("%d sujets émergents retenus pour qualification", len(topics))
    for t in topics:
        log.info("  %-34s IR=%.3f  G²=%7.1f  R=%3d B=%3d  %s", t.label[:34], t.disruption_index,
                 t.g2, t.n_recent, t.n_baseline, ",".join(t.source_types))

    entries, method = qualify(topics, protocol, use_llm=not args.no_llm)
    previous = store.previous_snapshot(as_of)
    compute_moves(entries, previous, protocol)
    store.save_snapshot(as_of, [{"label": e.label, "ring": e.ring} for e in entries])

    recent_start = as_of - timedelta(days=det["fenetre_recente_jours"])
    meta = {
        "as_of": as_of.date().isoformat(), "protocol_version": protocol["meta"]["version"], "method": method,
        "n_recent": sum(s.published > recent_start for s in signals),
        "n_baseline": sum(s.published <= recent_start for s in signals),
    }
    paths = write_outputs(entries, protocol, meta, args.out)
    for kind, path in paths.items():
        log.info("livrable %-5s : %s", kind, path)

    if not previous:
        log.info("premier radar : aucun mouvement à signaler (pas de radar antérieur)")
    elif alert := build_alert(entries, protocol):
        print(alert)
        if send(alert, protocol):
            log.info("alerte diffusée sur le canal d'équipe")
    return 0


def cmd_demo(args, protocol: dict, store: Store) -> int:
    with gzip.open(SAMPLE, "rt", encoding="utf-8") as f:
        signals = [Signal.from_dict(json.loads(line)) for line in f if line.strip()]
    inserted = store.upsert_signals(signals)
    log.info("jeu de démonstration chargé : %d signaux (%d nouveaux)", len(signals), inserted)
    return cmd_analyze(args, protocol, store)


def cmd_clusters(args, protocol: dict, store: Store) -> int:
    from radar.clusters import cluster_signals, clusters_markdown   # dépendance optionnelle

    det = protocol["detection"]
    as_of = datetime.fromisoformat(args.as_of).replace(tzinfo=timezone.utc) if args.as_of else store.latest_published()
    if as_of is None:
        log.error("base vide : lancer d'abord `collect` ou `demo`")
        return 1
    start = as_of - timedelta(days=det["fenetre_recente_jours"] + det["fenetre_reference_jours"])
    results = cluster_signals([s for s in store.signals_since(start) if s.published <= as_of], protocol,
                              as_of=as_of, n_clusters=args.k)
    for r in results:
        log.info("%s cluster %2d  G²=%7.1f  ×%-5.2f  nouveaux=%3.0f%%  %s", "⚑" if r.flagged else " ",
                 r.cluster_id, r.g2, r.growth, 100 * r.new_entrants, ", ".join(r.top_terms[:4]))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "clusters.md").write_text(clusters_markdown(results), encoding="utf-8")
    log.info("livrable clusters : %s", out / "clusters.md")
    return 0


def cmd_feedback(args, protocol: dict, store: Store) -> int:
    store.add_feedback(args.term, args.verdict, args.analyst, args.comment)
    log.info("verdict enregistré : « %s » = %s", args.term, args.verdict)
    return 0


def cmd_stats(args, protocol: dict, store: Store) -> int:
    print(json.dumps(store.stats(), ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="radar", description="Radar d'innovation automatisé (IA)")
    p.add_argument("--protocol", default=DEFAULT_PATH, help="chemin du protocole YAML")
    p.add_argument("--db", default=ROOT / "radar.db", help="base SQLite")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="command", required=True)

    def analysis_opts(sp):
        sp.add_argument("--out", default=ROOT / "output", help="répertoire des livrables")
        sp.add_argument("--as-of", help="date d'arrêté AAAA-MM-JJ (défaut : signal le plus récent)")
        sp.add_argument("--no-llm", action="store_true", help="qualification heuristique, sans appel au LLM")

    c = sub.add_parser("collect", help="collecter les signaux")
    c.add_argument("--full", action="store_true", help="recollecter toute la profondeur d'historique")
    c.add_argument("--export", help="exporter les signaux collectés en JSONL")
    c.set_defaults(func=cmd_collect)
    a = sub.add_parser("analyze", help="détecter, qualifier, restituer")
    analysis_opts(a)
    a.set_defaults(func=cmd_analyze)
    r = sub.add_parser("run", help="collect + analyze")
    r.add_argument("--full", action="store_true")
    r.add_argument("--export")
    analysis_opts(r)
    r.set_defaults(func=lambda args, p, s: cmd_collect(args, p, s) or cmd_analyze(args, p, s))
    d = sub.add_parser("demo", help="démonstration hors ligne")
    analysis_opts(d)
    d.set_defaults(func=cmd_demo)
    k = sub.add_parser("clusters", help="émergence par clustering thématique")
    k.add_argument("--out", default=ROOT / "output")
    k.add_argument("--as-of")
    k.add_argument("-k", type=int, help="nombre de clusters (défaut : √(n/2), borné à [8, 60])")
    k.set_defaults(func=cmd_clusters)
    f = sub.add_parser("feedback", help="verdict analyste sur un terme")
    f.add_argument("term")
    f.add_argument("verdict", choices=["pertinent", "bruit"])
    f.add_argument("--analyst", default="")
    f.add_argument("--comment", default="")
    f.set_defaults(func=cmd_feedback)
    s = sub.add_parser("stats", help="indicateurs de pilotage")
    s.set_defaults(func=cmd_stats)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)-7s %(message)s", datefmt="%H:%M:%S", stream=sys.stderr)
    logging.getLogger("httpx").setLevel(logging.WARNING)
    protocol = load_protocol(args.protocol)
    return args.func(args, protocol, Store(args.db))
