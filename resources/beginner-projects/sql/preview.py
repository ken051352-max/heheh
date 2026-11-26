"""Supplied query workspace before writing the ingestion exercise.

The default shop uses a curated subset of fixtures/orders.csv. The retake uses
a second synthetic shop with repeated names and order amounts.
This intentionally bypasses ingestion; it does not solve a learner TODO.
"""
import argparse
import csv
import json
from pathlib import Path
import sqlite3
import sys

HERE = Path(__file__).parent


def connect_preview(case="shop"):
    """Load one synthetic fixture, then hand the learner a read-only connection."""
    db = sqlite3.connect(":memory:", autocommit=True)
    try:
        db.execute("PRAGMA foreign_keys = ON")
        db.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
        if case == "retake":
            db.executescript((HERE / "fixtures/retake.sql").read_text(encoding="utf-8"))
        elif case == "shop":
            load_shop(db)
        else:
            raise ValueError(f"Unknown preview case: {case}")
        db.execute("PRAGMA query_only = ON")
        return db
    except Exception:
        db.close()
        raise


def load_shop(db):
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


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", type=Path, default=HERE / "preview.sql")
    parser.add_argument("--case", choices=("shop", "retake"), default="shop")
    args = parser.parse_args(argv)
    db = None
    try:
        sql = args.query.read_text(encoding="utf-8")
        db = connect_preview(args.case)
        cursor = db.execute(sql)
        print(json.dumps({"source": "curated synthetic preview", "case": args.case,
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
