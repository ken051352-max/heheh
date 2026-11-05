"""Local event-replay contracts in SQLite or DuckDB; no cluster guarantees."""
import argparse
import json
import sqlite3
from contextlib import closing
from datetime import datetime, timezone

try:
    import duckdb
except ModuleNotFoundError:
    duckdb = None


def connect(backend):
    if backend == "sqlite":
        return sqlite3.connect(":memory:", isolation_level=None)
    if backend == "duckdb":
        if duckdb is None:
            raise RuntimeError("DuckDB is not installed; install requirements.txt or use --backend sqlite")
        return duckdb.connect(":memory:")
    raise ValueError("Choose sqlite or duckdb")


def validate(row):
    expected = {"event_id", "account", "event_time", "amount_cents"}
    if set(row) != expected:
        raise ValueError("Schema fields changed")
    if not all(isinstance(row[k], str) and row[k] for k in ("event_id", "account", "event_time")):
        raise ValueError("Identifiers/time must be nonempty strings")
    if type(row["amount_cents"]) is not int or not 0 <= row["amount_cents"] <= 2**63 - 1:
        raise ValueError("amount_cents must be a nonnegative signed-BIGINT integer")
    event_time = datetime.fromisoformat(row["event_time"])
    if event_time.tzinfo is None:
        raise ValueError("Event time must carry a timezone")
    canonical_time = event_time.astimezone(timezone.utc).isoformat(timespec="microseconds")
    return row["event_id"], row["account"], canonical_time, row["amount_cents"]


def create_tables(connection):
    connection.execute("""CREATE TABLE events (
        event_id VARCHAR PRIMARY KEY, account VARCHAR NOT NULL,
        event_time VARCHAR NOT NULL, amount_cents BIGINT NOT NULL CHECK(amount_cents >= 0)
    )""")


def ingest(connection, rows):
    """Atomic accepted-row batch; quarantine invalid input and reject conflicting IDs."""
    quarantined, duplicates, late = [], 0, 0
    connection.execute("BEGIN TRANSACTION")
    try:
        for row in rows:
            try:
                event = validate(row)
            except (ValueError, TypeError) as error:
                quarantined.append({"row": row, "reason": str(error)})
                continue
            prior = connection.execute("SELECT * FROM events WHERE event_id = ?", [event[0]]).fetchone()
            if prior:
                if prior != event:
                    raise ValueError(f"Conflicting immutable event ID: {event[0]}")
                duplicates += 1
                continue
            previous_max = connection.execute("SELECT max(event_time) FROM events").fetchone()[0]
            if previous_max is not None and event[2] < previous_max:
                late += 1  # Policy: retain late events and recompute aggregates.
            connection.execute("INSERT INTO events VALUES (?, ?, ?, ?)", event)
        connection.execute("COMMIT")
    except Exception:
        connection.execute("ROLLBACK")
        raise
    return {"duplicates": duplicates, "late_retained": late, "quarantined": quarantined}


def totals(connection):
    return connection.execute("SELECT account, sum(amount_cents) FROM events GROUP BY account ORDER BY account").fetchall()


def run(backend="sqlite"):
    base = {"event_id": "e1", "account": "A", "event_time": "2026-01-01T12:00:00+00:00", "amount_cents": 100}
    batch = [base, dict(base), dict(base, event_id="e2", amount_cents=250),
             dict(base, event_id="e3", event_time="2026-01-01T11:00:00+00:00", amount_cents=50),
             dict(base, event_id="bad", amount_cents="oops")]
    with closing(connect(backend)) as connection:
        create_tables(connection)
        first = ingest(connection, batch)
        before = totals(connection)
        replay = ingest(connection, batch)
        assert totals(connection) == before == [("A", 400)]
        assert connection.execute("SELECT count(*) FROM events").fetchone()[0] == 3
        assert first["duplicates"] == 1 and first["late_retained"] == 1
        assert len(first["quarantined"]) == 1 and replay["duplicates"] == 4
        # A conflict after an earlier valid insert must roll back the entire accepted-row batch.
        try:
            ingest(connection, [dict(base, event_id="e4"), dict(base, amount_cents=999)])
        except ValueError:
            pass
        else:
            raise AssertionError("Conflicting duplicate was accepted")
        assert connection.execute("SELECT count(*) FROM events WHERE event_id = 'e4'").fetchone()[0] == 0
        assert totals(connection) == before
        version = sqlite3.sqlite_version if backend == "sqlite" else duckdb.__version__
        return {"backend": backend, "backend_version": version, "totals": before, "first_batch": first,
                "replay": replay, "conflict_rollback": "passed"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backend", choices=("sqlite", "duckdb"), default="sqlite")
    args = parser.parse_args()
    print(json.dumps(run(args.backend), indent=2))
