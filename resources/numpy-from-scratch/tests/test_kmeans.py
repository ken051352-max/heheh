import numpy as np
import pytest

from kmeans import KMeans

TRUE_CENTERS = np.array([[0.0, 0.0], [8.0, 8.0], [-8.0, 8.0]])


def blobs(n_per=100, seed=0):
    rng = np.random.default_rng(seed)
    X = np.vstack([c + rng.normal(scale=0.8, size=(n_per, 2)) for c in TRUE_CENTERS])
    y = np.repeat(np.arange(3), n_per)
    return X, y


def test_finds_the_true_centres():
    X, _ = blobs()
    m = KMeans(k=3, seed=0).fit(X)
    assert m.centers.shape == (3, 2)
    for c in TRUE_CENTERS:  # every true centre has a learned centre nearby
        assert np.min(np.linalg.norm(m.centers - c, axis=1)) < 0.5


def test_labels_are_a_consistent_partition():
    X, y = blobs()
    m = KMeans(k=3, seed=1).fit(X)
    assert m.labels_.shape == (len(X),)
    for j in range(3):  # each true blob maps to exactly one cluster id
        assert len(np.unique(m.labels_[y == j])) == 1
    assert len(np.unique(m.labels_)) == 3


def test_inertia_is_non_increasing_and_correct():
    X, _ = blobs()
    m = KMeans(k=3, seed=2).fit(X)
    h = np.array(m.inertia_history)
    assert len(h) >= 1 and np.all(np.diff(h) <= 1e-9)
    d2 = ((X[:, None, :] - m.centers[None]) ** 2).sum(-1).min(1).sum()
    assert m.inertia_ == pytest.approx(d2, rel=1e-6)


def test_predict_assigns_new_points_to_nearest_centre():
    X, _ = blobs()
    m = KMeans(k=3, seed=0).fit(X)
    new = TRUE_CENTERS + 0.1
    pred = m.predict(new)
    nearest = np.linalg.norm(new[:, None] - m.centers[None], axis=2).argmin(1)
    np.testing.assert_array_equal(pred, nearest)


def test_agrees_with_sklearn_inertia_if_installed():
    sk = pytest.importorskip("sklearn.cluster")
    X, _ = blobs()
    ours = KMeans(k=3, seed=0).fit(X)
    ref = sk.KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
    assert ours.inertia_ == pytest.approx(ref.inertia_, rel=1e-3)
