"""Worked SQLite investigation; deliberately small synthetic fixtures."""
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
    """Quarantine bad rows; skip identical duplicates; conflict rolls back batch."""
    duplicates, rejected, accepted = 0, [], 0
    db.execute("BEGIN")
    try:
        for line, row in enumerate(rows, start=2):
            try:
                if set(row) != {"order_id", "customer_id", "amount_cents"}:
                    raise ValueError("unexpected columns")
                order_id, customer = row["order_id"], row["customer_id"]
                raw_amount = row["amount_cents"]
                if not isinstance(order_id, str) or not order_id.strip():
                    raise ValueError("missing order ID")
                if not isinstance(customer, str) or not customer.strip():
                    raise ValueError("missing customer ID")
                if not isinstance(raw_amount, str) or not raw_amount.isascii() or not raw_amount.isdecimal():
                    raise ValueError("amount must contain nonnegative integer cents")
                amount = int(raw_amount)
                if amount > 2**63 - 1:
                    raise ValueError("amount exceeds SQLite integer range")
                if db.execute("SELECT 1 FROM customers WHERE customer_id=?", (customer,)).fetchone() is None:
                    raise ValueError("unknown customer")
            except (ValueError, TypeError, KeyError) as error:
                rejected.append({"line": line, "reason": str(error)})
                continue
            prior = db.execute("SELECT customer_id, amount_cents FROM orders WHERE order_id=?", (order_id,)).fetchone()
            if prior is not None:
                if prior != (customer, amount):
                    raise ValueError(f"conflicting duplicate order: {order_id}")
                duplicates += 1
                continue
            db.execute("INSERT INTO orders VALUES (?, ?, ?)", (order_id, customer, amount))
            accepted += 1
        db.execute("COMMIT")
    except Exception:
        db.execute("ROLLBACK")
        raise
    return {"accepted": accepted, "duplicates": duplicates, "rejected": rejected}


def report(db):
    """One row per customer, including no orders: ID, ordered, paid, outstanding."""
    return db.execute("""
        WITH order_totals AS (
            SELECT customer_id, sum(amount_cents) AS ordered FROM orders GROUP BY customer_id
        ), payment_totals AS (
            SELECT o.customer_id, sum(p.amount_cents) AS paid
            FROM payments p JOIN orders o ON p.order_id=o.order_id GROUP BY o.customer_id
        )
        SELECT c.customer_id, coalesce(o.ordered, 0), coalesce(p.paid, 0),
               coalesce(o.ordered, 0) - coalesce(p.paid, 0)
        FROM customers c LEFT JOIN order_totals o ON c.customer_id=o.customer_id
        LEFT JOIN payment_totals p ON c.customer_id=p.customer_id
        ORDER BY c.customer_id
    """).fetchall()


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
