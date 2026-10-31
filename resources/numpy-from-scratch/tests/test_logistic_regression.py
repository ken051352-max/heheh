import numpy as np
import pytest

from logistic_regression import LogisticRegression, sigmoid


def make_data(n=400, seed=0):
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, 2))
    true_w, true_b = np.array([2.0, -3.0]), 0.5
    p = 1 / (1 + np.exp(-(X @ true_w + true_b)))
    y = (rng.random(n) < p).astype(int)
    return X, y


def test_sigmoid_values_and_stability():
    assert sigmoid(np.array([0.0]))[0] == pytest.approx(0.5)
    out = sigmoid(np.array([-1000.0, 1000.0]))
    assert np.all(np.isfinite(out))
    assert out[0] == pytest.approx(0.0, abs=1e-12) and out[1] == pytest.approx(1.0)


def test_loss_decreases_and_shapes():
    X, y = make_data()
    m = LogisticRegression(lr=0.1, n_iters=500).fit(X, y)
    assert m.w.shape == (2,)
    assert len(m.loss_history) == 500
    assert m.loss_history[-1] < m.loss_history[0]
    assert m.predict(X).shape == (len(X),)
    assert set(np.unique(m.predict(X))) <= {0, 1}


def test_recovers_sign_of_true_weights_and_accuracy():
    X, y = make_data(n=2000)
    m = LogisticRegression(lr=0.5, n_iters=3000).fit(X, y)
    assert m.w[0] > 0 and m.w[1] < 0
    assert (m.predict(X) == y).mean() > 0.8


def test_matches_closed_form_gradient_at_zero():
    # One step of gradient descent from w=0, b=0 must equal -lr * X^T (0.5 - y) / n.
    X, y = make_data(n=50, seed=1)
    m = LogisticRegression(lr=1.0, n_iters=1).fit(X, y)
    expected = -(X.T @ (0.5 - y)) / len(y)
    np.testing.assert_allclose(m.w, expected, rtol=1e-6)


def test_agrees_with_sklearn_if_installed():
    sk = pytest.importorskip("sklearn.linear_model")
    X, y = make_data(n=1000)
    ours = LogisticRegression(lr=0.5, n_iters=5000).fit(X, y)
    ref = sk.LogisticRegression(C=1e6).fit(X, y)  # ~unregularised
    agree = (ours.predict(X) == ref.predict(X)).mean()
    assert agree > 0.98
