"""YOUR implementation: a decision-tree classifier in pure NumPy.

Pieces: an impurity function, a best-split search over (feature, threshold),
a recursive build with stopping rules, and a prediction traversal.
Run:  pytest -q tests/test_decision_tree.py
"""
import numpy as np  # noqa: F401


def gini(y):
    """Gini impurity 1 - sum_k p_k^2 of an integer label array (0.0 for an empty array)."""
    raise NotImplementedError


class DecisionTreeClassifier:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def depth(self):
        """Number of split levels (a single leaf has depth 0)."""
        raise NotImplementedError
