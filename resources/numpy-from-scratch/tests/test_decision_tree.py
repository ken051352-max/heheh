import numpy as np
import pytest

from decision_tree import DecisionTreeClassifier, gini


def test_gini():
    assert gini(np.array([1, 1, 1])) == pytest.approx(0.0)
    assert gini(np.array([0, 1])) == pytest.approx(0.5)
    assert gini(np.array([0, 1, 2])) == pytest.approx(2 / 3)
    assert gini(np.array([], dtype=int)) == pytest.approx(0.0)


def test_learns_a_single_threshold_with_a_stump():
    X = np.arange(10, dtype=float).reshape(-1, 1)
    y = (X[:, 0] > 4.5).astype(int)
    m = DecisionTreeClassifier(max_depth=1).fit(X, y)
    assert m.depth() == 1
    np.testing.assert_array_equal(m.predict(X), y)
    np.testing.assert_array_equal(m.predict(np.array([[4.4], [4.6]])), [0, 1])


def test_and_interaction_needs_depth_two():
    # y = x0 AND x1: one split cannot be perfect, two levels can.
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]] * 5, dtype=float)
    y = np.array([0, 0, 0, 1] * 5)
    stump = DecisionTreeClassifier(max_depth=1).fit(X, y)
    assert (stump.predict(X) == y).mean() < 1.0
    deep = DecisionTreeClassifier(max_depth=2).fit(X, y)
    assert (deep.predict(X) == y).all()


def test_greedy_tree_cannot_split_pure_xor():
    # Every root split on XOR has zero Gini gain, so greedy CART stops at a leaf.
    # This is correct behaviour, and a classic interview question.
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]] * 5, dtype=float)
    y = np.array([0, 1, 1, 0] * 5)
    m = DecisionTreeClassifier(max_depth=2).fit(X, y)
    assert m.depth() == 0


def test_max_depth_is_respected_and_unlimited_tree_fits_training_data():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 3))
    y = (X[:, 0] * X[:, 1] > 0).astype(int)
    shallow = DecisionTreeClassifier(max_depth=3).fit(X, y)
    assert shallow.depth() <= 3
    full = DecisionTreeClassifier().fit(X, y)
    assert (full.predict(X) == y).mean() == 1.0


def test_generalises_on_held_out_data():
    rng = np.random.default_rng(1)
    X = rng.uniform(-1, 1, size=(600, 2))
    y = ((X[:, 0] > 0.2) & (X[:, 1] < 0.5)).astype(int)
    m = DecisionTreeClassifier(max_depth=4).fit(X[:400], y[:400])
    assert (m.predict(X[400:]) == y[400:]).mean() > 0.95


def test_agrees_with_sklearn_if_installed():
    sk = pytest.importorskip("sklearn.tree")
    rng = np.random.default_rng(2)
    X = rng.normal(size=(300, 4))
    y = (X[:, 0] + X[:, 2] > 0).astype(int)
    ours = DecisionTreeClassifier(max_depth=3).fit(X, y)
    ref = sk.DecisionTreeClassifier(max_depth=3, random_state=0).fit(X, y)
    assert (ours.predict(X) == ref.predict(X)).mean() > 0.97
