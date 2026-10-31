"""Reference solution: CART-style decision tree classifier (Gini impurity)."""
import numpy as np


def gini(y):
    """Gini impurity 1 - sum_k p_k^2 of an integer label array."""
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    return float(1.0 - np.sum(p ** 2))


class _Node:
    __slots__ = ("feature", "threshold", "left", "right", "value")

    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature, self.threshold = feature, threshold
        self.left, self.right, self.value = left, right, value


class DecisionTreeClassifier:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def _best_split(self, X, y):
        n, d = X.shape
        parent = gini(y)
        best_gain, best = 0.0, (None, None)
        for f in range(d):
            values = np.unique(X[:, f])
            # candidate thresholds: midpoints between consecutive distinct values
            for t in (values[:-1] + values[1:]) / 2.0:
                left = X[:, f] <= t
                nl = left.sum()
                child = (nl * gini(y[left]) + (n - nl) * gini(y[~left])) / n
                gain = parent - child
                if gain > best_gain + 1e-12:
                    best_gain, best = gain, (f, t)
        return best

    def _build(self, X, y, depth):
        majority = int(np.bincount(y).argmax())
        if (len(np.unique(y)) == 1 or len(y) < self.min_samples_split
                or (self.max_depth is not None and depth >= self.max_depth)):
            return _Node(value=majority)
        f, t = self._best_split(X, y)
        if f is None:
            return _Node(value=majority)
        left = X[:, f] <= t
        return _Node(f, t, self._build(X[left], y[left], depth + 1),
                     self._build(X[~left], y[~left], depth + 1))

    def fit(self, X, y):
        self.root = self._build(np.asarray(X, dtype=float), np.asarray(y, dtype=int), 0)
        return self

    def _predict_one(self, x):
        node = self.root
        while node.value is None:
            node = node.left if x[node.feature] <= node.threshold else node.right
        return node.value

    def predict(self, X):
        return np.array([self._predict_one(x) for x in np.asarray(X, dtype=float)])

    def depth(self):
        def _d(node):
            return 0 if node.value is not None else 1 + max(_d(node.left), _d(node.right))
        return _d(self.root)
