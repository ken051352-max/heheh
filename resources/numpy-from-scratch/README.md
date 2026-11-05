[🏠 Roadmap home](../../README.md) · [🟧 Classical ML](../../curriculum/3-classical-ml.md#numpy-sprint) · [📦 Practitioner Stage 4](../../guides/practitioner-track.md#practitioner-track)

---

<a id="numpy-from-scratch"></a>
# 🧮 NumPy From Scratch: a unit-tested practice harness

This folder belongs to the **[Pure NumPy From Scratch Sprint](../../curriculum/3-classical-ml.md#numpy-sprint)**. Implement logistic regression alongside M10, K-Means alongside M11 and a tree alongside M12. The tests check selected contracts; passing them is evidence of those behaviors, not proof of correctness on every input. Compare with scikit-learn after your own implementation works.

| Algorithm | Your file | Tests | What the tests check |
|---|---|---|---|
| Logistic regression | [`starter/logistic_regression.py`](starter/logistic_regression.py) | [`tests/test_logistic_regression.py`](tests/test_logistic_regression.py) | stable sigmoid, falling loss, the exact first gradient step, recovered weight signs, agreement with sklearn |
| K-Means | [`starter/kmeans.py`](starter/kmeans.py) | [`tests/test_kmeans.py`](tests/test_kmeans.py) | recovered centres, a consistent partition, monotone Lloyd objective, nearest-centre prediction, duplicate-row/empty-cluster behavior, invalid inputs, seeds and refitting |
| Decision tree (CART, Gini) | [`starter/decision_tree.py`](starter/decision_tree.py) | [`tests/test_decision_tree.py`](tests/test_decision_tree.py) | Gini values, a one-split stump, depth limits, why greedy splitting can't solve XOR, held-out accuracy, sklearn agreement |

Video 1 (05:05) names these three algorithms. The [ML coding-interview video](../../guides/sources.md#citation-key) (W6, 07:51) repeats logistic regression and K-Means as typical from-scratch interview tasks.

## Run it

From this folder, create an environment with `python -m venv .venv`. Activate using `.venv\Scripts\Activate.ps1` in PowerShell or `source .venv/bin/activate` on Linux/macOS. Then:

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m pytest -q tests/test_kmeans.py
```

These commands test **your starter code**. Maintainers verify the shipped reference from the repository root:

```powershell
$env:NPFS_IMPL="reference"
python -m pytest -q resources/numpy-from-scratch/tests
Remove-Item Env:NPFS_IMPL
```

Linux/macOS equivalent: `NPFS_IMPL=reference python -m pytest -q resources/numpy-from-scratch/tests`. Clear the variable before assessing your starter; otherwise you can accidentally test the reference solution.

No local setup? [cs50.dev](https://cs50.dev/) and Google Colab both run `pytest` too.

Starter tests initially fail because implementations raise `NotImplementedError`. That is expected. The reference CI run should pass; it checks the harness without filling in the learner's files.

## Rules of the sprint

1. **Maths on paper first.** Write the forward pass, the loss and the update rule by hand before typing.
2. **No AI-generated code.** The [Foundations AI rule](../../curriculum/1-foundations.md#ai-usage-rule) still applies here. You may ask a model to *explain* a failing assertion. Don't ask it to write the fix.
3. **Attempt the implementation before opening `reference/`.** It holds worked solutions. Maintainers run the suite against it to check compatibility and selected algorithm invariants; tests themselves still need review.
4. **Then compare with sklearn.** Explain in your README every place where your result differs from [`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html), [`KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) or the [sklearn trees](https://scikit-learn.org/stable/modules/tree.html), for example regularisation defaults, `n_init` or tie-breaking.

## More free practice (optional)

**Completion evidence:** retain your mathematical derivation, tested implementation, exact environment/seed, a short results memo and a comparison with library behavior. Test names do not make an unregularized logistic model match a regularized default, nor make different K-Means initializations identical. Document such differences instead of changing tests merely to obtain green output. Your artifact may remain private.

| Resource | What it is | Notes |
|---|---|---|
| [Deep-ML](https://www.deep-ml.com/) | Browser-based ML coding problems with automatic grading (e.g. [K-Means](https://www.deep-ml.com/problems/17)) | Free problem set. Closest to an ML coding-interview round |
| [`ddbourgin/numpy-ml`](https://github.com/ddbourgin/numpy-ml) | Large library of reference NumPy implementations | **Read-only reference.** GPL-3.0 licensed and last updated in 2023, so read it *after* writing your own version and don't copy it into your projects |
| [NeetCode practice](https://neetcode.io/practice) | DSA problem lists | For the LeetCode-style round that many companies still run (see [findings](../../audit/v2026.7-research-findings.md#interview-prep)) |

---

[🏠 Roadmap home](../../README.md) · [🟧 Classical ML](../../curriculum/3-classical-ml.md#numpy-sprint)
