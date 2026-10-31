"""Reference solution: K-Means (Lloyd's algorithm) with k-means++ init and restarts."""
import numpy as np


class KMeans:
    def __init__(self, k, n_iters=300, tol=1e-6, n_init=10, seed=0):
        self.k = k
        self.n_iters = n_iters
        self.tol = tol
        self.n_init = n_init
        self.seed = seed
        self.centers = None
        self.labels_ = None
        self.inertia_ = None
        self.inertia_history = []

    @staticmethod
    def _sq_dists(X, centers):
        # (n, k) matrix of squared Euclidean distances, fully vectorised
        return ((X[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)

    def _init_pp(self, X, rng):
        centers = [X[rng.integers(len(X))]]
        for _ in range(1, self.k):
            d2 = self._sq_dists(X, np.array(centers)).min(axis=1)
            centers.append(X[rng.choice(len(X), p=d2 / d2.sum())])
        return np.array(centers)

    def _run(self, X, rng):
        centers = self._init_pp(X, rng)
        history = []
        for _ in range(self.n_iters):
            labels = self._sq_dists(X, centers).argmin(axis=1)          # assignment step
            new = np.array([X[labels == j].mean(axis=0) if np.any(labels == j) else centers[j]
                            for j in range(self.k)])                     # update step
            inertia = float(self._sq_dists(X, new).min(axis=1).sum())
            history.append(inertia)
            shift = np.abs(new - centers).max()
            centers = new
            if shift < self.tol:
                break
        labels = self._sq_dists(X, centers).argmin(axis=1)
        return centers, labels, history[-1], history

    def fit(self, X):
        X = np.asarray(X, dtype=float)
        rng = np.random.default_rng(self.seed)
        best = None
        for _ in range(self.n_init):
            run = self._run(X, rng)
            if best is None or run[2] < best[2]:
                best = run
        self.centers, self.labels_, self.inertia_, self.inertia_history = best
        return self

    def predict(self, X):
        return self._sq_dists(np.asarray(X, dtype=float), self.centers).argmin(axis=1)
