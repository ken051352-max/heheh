[🏠 Roadmap home](../../README.md) · [🟧 Classical ML](../../curriculum/3-classical-ml.md#numpy-sprint) · [📦 Practitioner Stage 4](../../guides/practitioner-track.md#practitioner-track)

---

<a id="numpy-from-scratch"></a>
# 🧮 NumPy From Scratch: a unit-tested practice harness

This folder belongs to the **[Pure NumPy From Scratch Sprint](../../curriculum/3-classical-ml.md#numpy-sprint)**. You implement three algorithms in plain NumPy. A test suite tells you when each one is correct. Only then do you move on to `scikit-learn`.

| Algorithm | Your file | Tests | What the tests check |
|---|---|---|---|
| Logistic regression | [`starter/logistic_regression.py`](starter/logistic_regression.py) | [`tests/test_logistic_regression.py`](tests/test_logistic_regression.py) | stable sigmoid, falling loss, the exact first gradient step, recovered weight signs, agreement with sklearn |
| K-Means | [`starter/kmeans.py`](starter/kmeans.py) | [`tests/test_kmeans.py`](tests/test_kmeans.py) | recovered centres, a consistent partition, inertia that never rises, nearest-centre `predict`, sklearn inertia |
| Decision tree (CART, Gini) | [`starter/decision_tree.py`](starter/decision_tree.py) | [`tests/test_decision_tree.py`](tests/test_decision_tree.py) | Gini values, a one-split stump, depth limits, why greedy splitting can't solve XOR, held-out accuracy, sklearn agreement |

Video 1 (05:05) names these three algorithms. The [ML coding-interview video](../../guides/sources.md#citation-key) (W6, 07:51) repeats logistic regression and K-Means as typical from-scratch interview tasks.

## Run it

```bash
# in this folder, inside a virtual environment (see M1, skill group 4)
uv venv && source .venv/bin/activate      # or: python -m venv .venv
uv pip install -r requirements.txt         # or: pip install -r requirements.txt
pytest -q                                  # runs against YOUR starter/ code
pytest -q tests/test_kmeans.py             # one algorithm at a time
```

No local setup? [cs50.dev](https://cs50.dev/) and Google Colab both run `pytest` too.

Every test fails with `NotImplementedError` until you write the code. That is expected.

## Rules of the sprint

1. **Maths on paper first.** Write the forward pass, the loss and the update rule by hand before typing.
2. **No AI-generated code.** The [Foundations AI rule](../../curriculum/1-foundations.md#ai-usage-rule) still applies here. You may ask a model to *explain* a failing assertion. Don't ask it to write the fix.
3. **Don't open `reference/` until your tests pass.** It holds model solutions. Maintainers (and the staged CI workflow) run `NPFS_IMPL=reference pytest -q` to prove the tests are correct.
4. **Then compare with sklearn.** Explain in your README every place where your result differs from [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) or the [sklearn trees](https://scikit-learn.org/stable/modules/tree.html), for example regularisation defaults, `n_init` or tie-breaking.

## More free practice (optional)

| Resource | What it is | Notes |
|---|---|---|
| [Deep-ML](https://www.deep-ml.com/) | Browser-based ML coding problems with automatic grading (e.g. [K-Means](https://www.deep-ml.com/problems/17)) | Free problem set. Closest to an ML coding-interview round |
| [`ddbourgin/numpy-ml`](https://github.com/ddbourgin/numpy-ml) | Large library of reference NumPy implementations | **Read-only reference.** GPL-3.0 licensed and last updated in 2023, so read it *after* writing your own version and don't copy it into your projects |
| [NeetCode practice](https://neetcode.io/practice) | DSA problem lists | For the LeetCode-style round that many companies still run (see [findings](../../audit/v2026.7-research-findings.md#interview-prep)) |

---

[🏠 Roadmap home](../../README.md) · [🟧 Classical ML](../../curriculum/3-classical-ml.md#numpy-sprint)
