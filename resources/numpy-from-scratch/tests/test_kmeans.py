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


@pytest.mark.parametrize("X", [np.ones((6, 2)), np.array([[0., 0.], [0., 0.], [2., 2.], [2., 2.]])])
def test_duplicate_points_do_not_break_kmeans_plus_plus(X):
    m = KMeans(k=3, seed=7).fit(X)
    assert np.isfinite(m.centers).all()
    assert m.inertia_ == pytest.approx(0.0)
    np.testing.assert_allclose(m.centers[m.predict(X)], X)


@pytest.mark.parametrize("kwargs", [
    {"k": 0}, {"k": 1.5}, {"k": True}, {"k": 2, "n_iters": 0},
    {"k": 2, "n_init": 0}, {"k": 2, "tol": -1}, {"k": 2, "tol": np.nan},
])
def test_invalid_configuration_is_rejected(kwargs):
    with pytest.raises(ValueError):
        KMeans(**kwargs).fit(np.zeros((3, 2)))


@pytest.mark.parametrize("X", [[], [[1]], [[1, np.nan], [2, 3]], [[1, np.inf], [2, 3]], [1, 2, 3]])
def test_invalid_training_data_is_rejected(X):
    with pytest.raises(ValueError):
        KMeans(k=2).fit(X)


def test_prediction_requires_fit_and_matching_features():
    m = KMeans(k=2)
    with pytest.raises(ValueError):
        m.predict([[0, 0]])
    m.fit([[0, 0], [1, 1]])
    with pytest.raises(ValueError):
        m.predict([[0, 0, 0]])


def test_seed_reproduces_solution_and_refit_replaces_training_state():
    X, _ = blobs()
    first = KMeans(k=3, seed=8).fit(X)
    second = KMeans(k=3, seed=8).fit(X)
    np.testing.assert_array_equal(first.centers, second.centers)
    first.fit(np.ones((4, 2)))
    assert first.labels_.shape == (4,)
    assert first.inertia_ == pytest.approx(0.0)
