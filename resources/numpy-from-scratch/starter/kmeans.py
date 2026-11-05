"""YOUR implementation: K-Means clustering in pure NumPy.

Lloyd's algorithm = repeat (assignment step, update step) until centres stop moving.
Use several random restarts (n_init) and keep the run with the lowest inertia.
Input contract: finite nonempty 2D training data; positive integer k/n_iters/n_init;
k <= n_samples; finite nonnegative tol. Invalid inputs raise ValueError.
Duplicate rows are allowed. If k exceeds the number of distinct points, duplicate
centres and unused labels are valid; zero total k-means++ distance must not divide
by zero. predict requires a fitted model and the same finite feature count.
Run:  pytest -q tests/test_kmeans.py
"""
import numpy as np  # noqa: F401


class KMeans:
    def __init__(self, k, n_iters=300, tol=1e-6, n_init=10, seed=0):
        self.k = k
        self.n_iters = n_iters
        self.tol = tol
        self.n_init = n_init
        self.seed = seed
        self.centers = None         # shape (k, n_features)
        self.labels_ = None         # shape (n_samples,)
        self.inertia_ = None        # sum of squared distances to the nearest centre
        self.inertia_history = []   # inertia after each iteration of the best run

    def fit(self, X):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError
