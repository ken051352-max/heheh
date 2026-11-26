"""The supplied preview must work before learner ingestion TODOs are filled."""
import importlib.util
import json
from pathlib import Path
import sqlite3
import pytest

SPEC = importlib.util.spec_from_file_location(
    "sql_preview", Path(__file__).parents[1] / "sql" / "preview.py")
preview = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preview)


def test_curated_data_reconciles_and_preserves_zero_order_customer():
    db = preview.connect_preview()
    try:
        assert db.execute("SELECT count(*), sum(amount_cents) FROM orders").fetchone() == (3, 2500)
        assert db.execute("SELECT sum(amount_cents) FROM payments").fetchone() == (2300,)
        assert db.execute("SELECT customer_id FROM customers WHERE customer_id NOT IN "
                          "(SELECT customer_id FROM orders)").fetchall() == [("C",)]
        with pytest.raises(sqlite3.OperationalError):
            db.execute("UPDATE orders SET amount_cents = 0")
        assert db.execute("SELECT sum(amount_cents) FROM orders").fetchone() == (2500,)
    finally:
        db.close()


def test_starting_query_runs_without_learner_implementation(capsys):
    assert preview.main([]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["rows"] == [["o1", "A", 1200], ["o2", "A", 800], ["o3", "B", 500]]


def test_missing_and_bad_queries_report_failure(tmp_path, capsys):
    query = tmp_path / "query.sql"
    assert preview.main([str(query)]) == 2
    assert capsys.readouterr().err
    query.write_text("SELECT missing_column FROM orders", encoding="utf-8")
    assert preview.main([str(query)]) == 2
    output = capsys.readouterr()
    assert output.err and not output.out


def test_retake_runs_the_same_query_on_a_new_read_only_fixture(tmp_path, capsys):
    query = tmp_path / "report.sql"
    query.write_text(
        "SELECT c.customer_id, COUNT(o.order_id), COALESCE(SUM(o.amount_cents),0) "
        "FROM customers AS c LEFT JOIN orders AS o USING (customer_id) "
        "GROUP BY c.customer_id ORDER BY c.customer_id", encoding="utf-8")
    assert preview.main(["--case", "retake", str(query)]) == 0
    assert json.loads(capsys.readouterr().out)["rows"] == [
        ["1", 2, 1200], ["2", 2, 600], ["3", 0, 0], ["4", 0, 0]]
    query.write_text("DELETE FROM orders", encoding="utf-8")
    assert preview.main(["--case", "retake", str(query)]) == 2
