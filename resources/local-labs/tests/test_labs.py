"""Deterministic identification and event-ledger tests; no network or population claims."""
import importlib.util
import math
from pathlib import Path
import unittest


def load(name):
    path = Path(__file__).parents[1] / (name + ".py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


causal = load("causal_inference")
pipeline = load("distributed_data")


class CausalIdentification(unittest.TestCase):
    def test_adjustment_recovers_known_effect_despite_confounding(self):
        # Imbalance creates a naive contrast of 3.8; each stratum's effect is 2.
        rows = [(0, 0, 0)] * 8 + [(0, 1, 2)] * 2 + [(1, 0, 3)] * 2 + [(1, 1, 5)] * 8
        self.assertAlmostEqual(causal.difference(rows)[0], 3.8)
        self.assertEqual(causal.adjusted(rows), (2.0, 0.0))

    def test_no_overlap_is_reported_instead_of_an_estimate(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            causal.adjusted([(0, 0, 0)] * 4 + [(1, 1, 5)] * 4)

    def test_known_normal_design_and_monotonicity(self):
        base = causal.sample_size_per_arm(1, 0.5)
        self.assertEqual(base, 63)
        self.assertGreater(causal.sample_size_per_arm(1, 0.25), base)
        self.assertGreater(causal.sample_size_per_arm(2, 0.5), base)
        self.assertGreater(causal.sample_size_per_arm(1, 0.5, power=0.9), base)
        self.assertGreater(causal.sample_size_per_arm(1, 0.5, alpha=0.01), base)

    def test_invalid_design_parameters_are_rejected(self):
        for sigma, mde in ((0, 1), (1, 0), (-1, 1), (math.inf, 1), (1, math.inf)):
            with self.subTest(sigma=sigma, mde=mde), self.assertRaises(ValueError):
                causal.sample_size_per_arm(sigma, mde)
        with self.assertRaises(ValueError):
            causal.sample_size_per_arm(1, 1, power=1)

    def test_generator_reproducibility_and_declared_population(self):
        rows = causal.generate(100, 42, False, noise=0)
        self.assertEqual(rows, causal.generate(100, 42, False, noise=0))
        self.assertEqual(sum(x for x, _, _ in rows), 50)
        for x, t, y in rows:
            self.assertEqual(y, 3 * x + 2 * t)

    def test_generator_requires_adequate_even_sample(self):
        for n in (0, 39, 41):
            with self.subTest(n=n), self.assertRaises(ValueError):
                causal.generate(n, 0, True)


class EventLedgerContracts:
    """Run identical behavior contracts against both supported SQL backends."""
    def setUp(self):
        self.db = pipeline.connect(self.backend)
        self.addCleanup(self.db.close)
        pipeline.create_tables(self.db)
        self.base = {"event_id": "one", "account": "A", "event_time": "2026-01-01T12:00:00+00:00",
                     "amount_cents": 100}

    def test_replay_keeps_totals_and_isolates_accounts(self):
        rows = [self.base, dict(self.base, event_id="two", account="B", amount_cents=250)]
        pipeline.ingest(self.db, rows)
        result = pipeline.ingest(self.db, rows)
        self.assertEqual(result["duplicates"], 2)
        self.assertEqual(pipeline.totals(self.db), [("A", 100), ("B", 250)])

    def test_equivalent_timezone_is_same_event(self):
        pipeline.ingest(self.db, [self.base])
        equivalent = dict(self.base, event_time="2026-01-01T13:00:00+01:00")
        self.assertEqual(pipeline.ingest(self.db, [equivalent])["duplicates"], 1)

    def test_late_arrival_is_retained_and_counted(self):
        pipeline.ingest(self.db, [self.base])
        late = dict(self.base, event_id="late", event_time="2025-12-31T10:00:00+00:00")
        self.assertEqual(pipeline.ingest(self.db, [late])["late_retained"], 1)
        self.assertEqual(pipeline.totals(self.db), [("A", 200)])

    def test_invalid_rows_are_quarantined_and_valid_rows_committed(self):
        bad_rows = [dict(self.base, amount_cents=True), dict(self.base, amount_cents=-1),
                    dict(self.base, amount_cents=2**63), dict(self.base, event_time="2026-01-01"),
                    dict(self.base, extra="schema drift"), None]
        result = pipeline.ingest(self.db, [*bad_rows, self.base])
        self.assertEqual(len(result["quarantined"]), len(bad_rows))
        self.assertEqual(pipeline.totals(self.db), [("A", 100)])

    def test_conflict_rolls_back_an_earlier_valid_insert(self):
        pipeline.ingest(self.db, [self.base])
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            pipeline.ingest(self.db, [dict(self.base, event_id="new"), dict(self.base, amount_cents=900)])
        self.assertEqual(pipeline.totals(self.db), [("A", 100)])
        self.assertEqual(self.db.execute("SELECT count(*) FROM events WHERE event_id='new'").fetchone()[0], 0)
        # The connection remains usable after rollback.
        pipeline.ingest(self.db, [dict(self.base, event_id="after")])
        self.assertEqual(pipeline.totals(self.db), [("A", 200)])

    def test_schema_change_for_same_event_is_not_silently_overwritten(self):
        pipeline.ingest(self.db, [self.base])
        with self.assertRaisesRegex(ValueError, "Conflicting"):
            pipeline.ingest(self.db, [dict(self.base, account="B")])
        self.assertEqual(pipeline.totals(self.db), [("A", 100)])


class SQLiteEventLedger(EventLedgerContracts, unittest.TestCase):
    backend = "sqlite"


@unittest.skipIf(pipeline.duckdb is None, "DuckDB unavailable; install resources/local-labs/requirements.txt to run these six contracts")
class DuckDBEventLedger(EventLedgerContracts, unittest.TestCase):
    backend = "duckdb"


if __name__ == "__main__":
    unittest.main()
