"""Persistance SQLite : mémoire longue du dispositif de veille.

La détection d'émergence compare une période récente à une période de
référence : elle exige donc un historique. Le stockage conserve aussi les
radars successifs (pour calculer les mouvements) et les retours des analystes
(boucle de rétroaction humaine).
"""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from radar.models import Signal

SCHEMA = """
CREATE TABLE IF NOT EXISTS signals (
    id           TEXT PRIMARY KEY,
    source       TEXT NOT NULL,
    source_type  TEXT NOT NULL,
    title        TEXT NOT NULL,
    summary      TEXT,
    url          TEXT NOT NULL,
    published    TEXT NOT NULL,
    authors      TEXT,
    axis         TEXT,
    engagement   REAL DEFAULT 0,
    credibility  REAL DEFAULT 0.5,
    collected_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_signals_published ON signals(published);

CREATE TABLE IF NOT EXISTS radar_snapshots (
    run_at  TEXT PRIMARY KEY,
    entries TEXT NOT NULL            -- JSON : liste de RadarEntry
);

CREATE TABLE IF NOT EXISTS feedback (
    term       TEXT PRIMARY KEY,
    verdict    TEXT NOT NULL CHECK (verdict IN ('pertinent', 'bruit')),
    analyst    TEXT,
    comment    TEXT,
    decided_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS runs (
    run_at     TEXT PRIMARY KEY,
    collected  INTEGER,
    inserted   INTEGER,
    errors     TEXT
);
"""


class Store:
    def __init__(self, path: str | Path = "radar.db"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(SCHEMA)

    # --- signaux ---------------------------------------------------------
    def upsert_signals(self, signals: list[Signal]) -> int:
        """Insère les nouveaux signaux ; met à jour l'engagement des signaux connus. Renvoie le nb d'insertions."""
        now = datetime.now(timezone.utc).isoformat()
        before = self.count()
        self.conn.executemany(
            """INSERT INTO signals VALUES (:id, :source, :source_type, :title, :summary, :url,
                                           :published, :authors, :axis, :engagement, :credibility, :now)
               ON CONFLICT(id) DO UPDATE SET engagement = excluded.engagement""",
            [{**s.to_dict(), "authors": json.dumps(s.authors), "now": now} for s in signals],
        )
        self.conn.commit()
        return self.count() - before

    def signals_since(self, since: datetime) -> list[Signal]:
        rows = self.conn.execute(
            "SELECT * FROM signals WHERE published >= ? ORDER BY published", (since.isoformat(),)
        )
        return [
            Signal(
                id=r["id"], source=r["source"], source_type=r["source_type"], title=r["title"],
                summary=r["summary"] or "", url=r["url"], published=datetime.fromisoformat(r["published"]),
                authors=json.loads(r["authors"] or "[]"), axis=r["axis"],
                engagement=r["engagement"], credibility=r["credibility"],
            )
            for r in rows
        ]

    def count(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM signals").fetchone()[0]

    def latest_published(self) -> datetime | None:
        row = self.conn.execute("SELECT MAX(published) FROM signals").fetchone()[0]
        return datetime.fromisoformat(row) if row else None

    # --- radars successifs ----------------------------------------------
    def save_snapshot(self, run_at: datetime, entries: list[dict]) -> None:
        self.conn.execute("INSERT OR REPLACE INTO radar_snapshots VALUES (?, ?)",
                          (run_at.isoformat(), json.dumps(entries, ensure_ascii=False)))
        self.conn.commit()

    def previous_snapshot(self, before: datetime) -> list[dict]:
        row = self.conn.execute(
            "SELECT entries FROM radar_snapshots WHERE run_at < ? ORDER BY run_at DESC LIMIT 1",
            (before.isoformat(),),
        ).fetchone()
        return json.loads(row[0]) if row else []

    # --- boucle de rétroaction ------------------------------------------
    def add_feedback(self, term: str, verdict: str, analyst: str = "", comment: str = "") -> None:
        self.conn.execute("INSERT OR REPLACE INTO feedback VALUES (?, ?, ?, ?, ?)",
                          (term.lower(), verdict, analyst, comment, datetime.now(timezone.utc).isoformat()))
        self.conn.commit()

    def feedback(self) -> dict[str, str]:
        return {r["term"]: r["verdict"] for r in self.conn.execute("SELECT term, verdict FROM feedback")}

    # --- journal d'exécution (traçabilité) ------------------------------
    def log_run(self, run_at: datetime, collected: int, inserted: int, errors: list[str]) -> None:
        self.conn.execute("INSERT OR REPLACE INTO runs VALUES (?, ?, ?, ?)",
                          (run_at.isoformat(), collected, inserted, json.dumps(errors, ensure_ascii=False)))
        self.conn.commit()

    def stats(self) -> dict:
        q = self.conn.execute
        return {
            "signaux_total": self.count(),
            "par_source": dict(q("SELECT source, COUNT(*) FROM signals GROUP BY source ORDER BY 2 DESC").fetchall()),
            "par_axe": dict(q("SELECT COALESCE(axis, 'hors périmètre'), COUNT(*) FROM signals GROUP BY 1").fetchall()),
            "verdicts": dict(q("SELECT verdict, COUNT(*) FROM feedback GROUP BY verdict").fetchall()),
            "executions": [dict(r) for r in q("SELECT * FROM runs ORDER BY run_at DESC LIMIT 10")],
            "radars_archives": q("SELECT COUNT(*) FROM radar_snapshots").fetchone()[0],
        }
