"""Your sql project. Supplied adapter/runner code is scaffolding; implement TODOs."""
import csv
import json
from pathlib import Path
import sqlite3

HERE = Path(__file__).parent


def connect():
    db = sqlite3.connect(":memory:", autocommit=True)
    db.execute("PRAGMA foreign_keys = ON")
    if db.execute("PRAGMA foreign_keys").fetchone()[0] != 1:
        db.close()
        raise RuntimeError("this SQLite build lacks foreign-key enforcement")
    db.executescript((HERE / "schema.sql").read_text(encoding="utf-8"))
    return db


def ingest_orders(db, rows):
    """TODO: Rows use string CSV fields. Validate IDs, whole nonnegative cents and customer existence. Reject malformed rows with line/reason; count identical duplicates; atomically roll back conflicts. Return accepted, duplicates and rejected."""
    raise NotImplementedError("Implement ingest_orders")


def report(db):
    """TODO: Return sorted customer rows (customer_id, ordered_cents, paid_cents, outstanding_cents). Include customers with no orders. Avoid multiplying order totals by payment rows; first decide the grain of each aggregate."""
    raise NotImplementedError("Implement report")


def read_csv(name):
    with (HERE / "fixtures" / name).open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def demo():
    db = connect()
    try:
        db.executemany("INSERT INTO customers VALUES (?, ?)",
                       [(r["customer_id"], r["name"]) for r in read_csv("customers.csv")])
        load = ingest_orders(db, read_csv("orders.csv"))
        db.executemany("INSERT INTO payments VALUES (?, ?, ?)",
                       [(r["payment_id"], r["order_id"], int(r["amount_cents"])) for r in read_csv("payments.csv")])
        query = "SELECT order_id FROM orders WHERE customer_id = ?"
        before = db.execute("EXPLAIN QUERY PLAN " + query, ("A",)).fetchall()
        db.execute("CREATE INDEX orders_customer ON orders(customer_id)")
        after = db.execute("EXPLAIN QUERY PLAN " + query, ("A",)).fetchall()
        return {"source": "synthetic fixture", "sqlite_version": sqlite3.sqlite_version,
                "load": load, "customers": report(db), "plan_before": before, "plan_after": after}
    finally:
        db.close()


if __name__ == "__main__":
    print(json.dumps(demo(), indent=2))
