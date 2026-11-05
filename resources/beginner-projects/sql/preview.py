"""Supplied query workspace before writing the ingestion exercise.

Clean orders below are a curated synthetic subset of fixtures/orders.csv.
This intentionally bypasses ingestion; it does not solve a learner TODO.
"""
import argparse
import csv
import json
from pathlib import Path
import sqlite3
import sys

HERE = Path(__file__).parent


def connect_preview():
    db = sqlite3.connect(":memory:", autocommit=True)
    try:
        db.execute("PRAGMA foreign_keys = ON")
        db.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
        with (HERE / "fixtures/customers.csv").open(encoding="utf-8", newline="") as stream:
            customers = list(csv.DictReader(stream))
        db.executemany("INSERT INTO customers VALUES (?, ?)",
                       [(r["customer_id"], r["name"]) for r in customers])
        # Reviewed clean rows, not an ingestion algorithm to copy.
        db.executemany("INSERT INTO orders VALUES (?, ?, ?)",
                       [("o1", "A", 1200), ("o2", "A", 800), ("o3", "B", 500)])
        with (HERE / "fixtures/payments.csv").open(encoding="utf-8", newline="") as stream:
            payments = list(csv.DictReader(stream))
        db.executemany("INSERT INTO payments VALUES (?, ?, ?)",
                       [(r["payment_id"], r["order_id"], int(r["amount_cents"])) for r in payments])
        db.execute("PRAGMA query_only = ON")
        return db
    except Exception:
        db.close()
        raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", type=Path, default=HERE / "preview.sql")
    args = parser.parse_args(argv)
    db = None
    try:
        sql = args.query.read_text(encoding="utf-8")
        db = connect_preview()
        cursor = db.execute(sql)
        print(json.dumps({"source": "curated synthetic preview",
                          "columns": [c[0] for c in cursor.description] if cursor.description else [],
                          "rows": cursor.fetchall()}))
    except (OSError, UnicodeError, sqlite3.Error) as error:
        print(f"Query failed: {error}", file=sys.stderr)
        return 2
    finally:
        if db is not None:
            db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
