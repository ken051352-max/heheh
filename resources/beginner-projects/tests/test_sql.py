import sqlite3
import pytest


@pytest.fixture
def investigation(project):
    lab = project("sql")
    db = lab.connect()
    db.executemany("INSERT INTO customers VALUES (?, ?)", [("A", "Library"), ("B", "Club"), ("C", "No orders")])
    yield lab, db
    db.close()


def row(order="one", customer="A", amount="100"):
    return {"order_id": order, "customer_id": customer, "amount_cents": amount}


def test_fixture_reconciliation_includes_zero_order_customer(project):
    result = project("sql").demo()
    assert result["customers"] == [("A", 2000, 1800, 200), ("B", 500, 500, 0), ("C", 0, 0, 0)]
    assert result["load"]["accepted"] == 3
    assert result["load"]["duplicates"] == 1
    assert len(result["load"]["rejected"]) == 3


def test_replay_preserves_totals(investigation):
    lab, db = investigation
    rows = [row(), row("two", "B", "250")]
    lab.ingest_orders(db, rows)
    before = lab.report(db)
    assert lab.ingest_orders(db, rows)["duplicates"] == 2
    assert lab.report(db) == before


def test_split_payments_do_not_multiply_orders(investigation):
    lab, db = investigation
    lab.ingest_orders(db, [row(amount="1000")])
    db.executemany("INSERT INTO payments VALUES (?, ?, ?)", [("p1", "one", 200), ("p2", "one", 300)])
    assert lab.report(db)[0] == ("A", 1000, 500, 500)


def test_two_identical_amounts_are_not_deduplicated(investigation):
    lab, db = investigation
    lab.ingest_orders(db, [row(), row("two")])
    assert lab.report(db)[0] == ("A", 200, 0, 200)


@pytest.mark.parametrize("bad", [
    row(amount=""), row(amount="-1"), row(amount="1.5"), row(amount=str(2**63)),
    row(customer="unknown"), row(order=""), row(amount=True), None,
])
def test_bad_rows_quarantined_without_losing_valid_row(investigation, bad):
    lab, db = investigation
    result = lab.ingest_orders(db, [bad, row("valid")])
    assert result["accepted"] == 1 and len(result["rejected"]) == 1
    assert result["rejected"][0]["reason"]
    assert lab.report(db)[0] == ("A", 100, 0, 100)


def test_conflicting_duplicate_rolls_back_earlier_insert(investigation):
    lab, db = investigation
    lab.ingest_orders(db, [row()])
    with pytest.raises(ValueError):
        lab.ingest_orders(db, [row("new"), row(amount="999")])
    assert db.execute("SELECT order_id FROM orders ORDER BY order_id").fetchall() == [("one",)]
    assert lab.ingest_orders(db, [row("after")])["accepted"] == 1


def test_keys_foreign_keys_and_amount_constraints(investigation):
    lab, db = investigation
    lab.ingest_orders(db, [row()])
    invalid = [
        ("INSERT INTO orders VALUES (?, ?, ?)", ("one", "A", 100)),
        ("INSERT INTO orders VALUES (?, ?, ?)", ("bad", "missing", 100)),
        ("INSERT INTO orders VALUES (?, ?, ?)", ("bad", "A", -1)),
        ("INSERT INTO orders VALUES (?, ?, ?)", ("bad", "A", 1.5)),
        ("INSERT INTO payments VALUES (?, ?, ?)", ("p", "missing", 100)),
    ]
    for sql, parameters in invalid:
        with pytest.raises(sqlite3.IntegrityError):
            db.execute(sql, parameters)
