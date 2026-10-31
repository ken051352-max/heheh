"""Reference solution: binary logistic regression with batch gradient descent.

Do not open this file until your own starter/ implementation passes the tests.
"""
import numpy as np


def sigmoid(z):
    """Numerically stable logistic function, elementwise."""
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)
    pos = z >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-z[pos]))
    ez = np.exp(z[~pos])
    out[~pos] = ez / (1.0 + ez)
    return out


def binary_cross_entropy(y_true, p, eps=1e-12):
    p = np.clip(p, eps, 1 - eps)
    return float(-np.mean(y_true * np.log(p) + (1 - y_true) * np.log(1 - p)))


class LogisticRegression:
    def __init__(self, lr=0.1, n_iters=2000, l2=0.0):
        self.lr = lr
        self.n_iters = n_iters
        self.l2 = l2
        self.w = None
        self.b = 0.0
        self.loss_history = []

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        n, d = X.shape
        self.w = np.zeros(d)
        self.b = 0.0
        self.loss_history = []
        for _ in range(self.n_iters):
            p = sigmoid(X @ self.w + self.b)          # forward
            err = p - y                               # dL/dz for BCE + sigmoid
            dw = X.T @ err / n + self.l2 * self.w     # gradient w.r.t. weights
            db = err.mean()                           # gradient w.r.t. bias
            self.w -= self.lr * dw                    # update
            self.b -= self.lr * db
            self.loss_history.append(binary_cross_entropy(y, p))
        return self

    def predict_proba(self, X):
        return sigmoid(np.asarray(X, dtype=float) @ self.w + self.b)

    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)
