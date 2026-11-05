"""Reference solution: K-Means (Lloyd's algorithm) with k-means++ init and restarts."""
import numpy as np


class KMeans:
    def __init__(self, k, n_iters=300, tol=1e-6, n_init=10, seed=0):
        for name, value in (("k", k), ("n_iters", n_iters), ("n_init", n_init)):
            if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        if not isinstance(tol, (int, float, np.integer, np.floating)) or not np.isfinite(tol) or tol < 0:
            raise ValueError("tol must be finite and nonnegative")
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
            total = d2.sum()
            # All distinct locations are already represented. Duplicate centres
            # are valid: with fewer than k distinct points some labels stay unused.
            index = rng.integers(len(X)) if total == 0 else rng.choice(len(X), p=d2 / total)
            centers.append(X[index])
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
        if X.ndim != 2 or min(X.shape) == 0 or not np.isfinite(X).all():
            raise ValueError("X must be a nonempty finite 2D array")
        if self.k > len(X):
            raise ValueError("k cannot exceed the number of samples")
        rng = np.random.default_rng(self.seed)
        best = None
        for _ in range(self.n_init):
            run = self._run(X, rng)
            if best is None or run[2] < best[2]:
                best = run
        self.centers, self.labels_, self.inertia_, self.inertia_history = best
        return self

    def predict(self, X):
        if self.centers is None:
            raise ValueError("fit must be called before predict")
        X = np.asarray(X, dtype=float)
        if X.ndim != 2 or X.shape[1] != self.centers.shape[1] or not np.isfinite(X).all():
            raise ValueError("X must be finite and have the fitted feature count")
        return self._sq_dists(X, self.centers).argmin(axis=1)
