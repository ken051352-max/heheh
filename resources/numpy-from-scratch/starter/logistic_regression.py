"""YOUR implementation: binary logistic regression in pure NumPy.

Write the maths on paper first (forward pass, binary cross-entropy, gradient),
then fill in each method. Run:  pytest -q tests/test_logistic_regression.py
"""
import numpy as np  # noqa: F401  (you will need it)


def sigmoid(z):
    """Elementwise 1 / (1 + exp(-z)). Must not overflow for z = -1000 or +1000."""
    raise NotImplementedError


class LogisticRegression:
    def __init__(self, lr=0.1, n_iters=2000, l2=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.l2 = l2
        self.w = None          # shape (n_features,)
        self.b = 0.0
        self.loss_history = []  # append the training loss once per iteration

    def fit(self, X, y):
        """Batch gradient descent: forward -> dw, db -> update. Return self."""
        raise NotImplementedError

    def predict_proba(self, X):
        raise NotImplementedError

    def predict(self, X, threshold=0.5):
        raise NotImplementedError
