"""Offline retrieval lab contracts on cases separate from the demonstration."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("retrieval", Path(__file__).parents[1] / "retrieval.py")
retrieval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retrieval)


class RetrievalContracts(unittest.TestCase):
    def test_scope_ties_and_no_overlap(self):
        docs = [retrieval.Document("b", "Room", "blue"), retrieval.Document("a", "Room", "green"),
                retrieval.Document("c", "Room", "blue", "staff")]
        self.assertEqual(retrieval.retrieve("room", docs, "public", include_passage=False), ["a", "b"])
        self.assertEqual(retrieval.retrieve("BLUE", docs, "public", include_passage=True), ["b"])
        self.assertEqual(retrieval.retrieve("blue", docs, "staff", include_passage=True), ["b", "c"])
        self.assertEqual(retrieval.retrieve("blue", docs, "public", include_passage=False), [])

    def test_wrong_answer_and_false_abstention_have_separate_denominators(self):
        cases = [("one", "a"), ("two", "b"), ("three", None), ("four", None)]
        scores = retrieval.evaluate(cases, [[], ["a"], [], ["c"]])
        self.assertEqual((scores["hits_at_1"], scores["answerable"]), (0, 2))
        self.assertEqual((scores["correct_abstentions"], scores["unanswerable"]), (1, 2))
