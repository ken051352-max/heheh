[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟨 Statistics & Data (M6–M8b)](2-statistics-and-data.md) · [🟦 Probabilistic ML (M13–M14) →](4-probabilistic-ml.md)

---

# 🟧 CLASSICAL MACHINE LEARNING STRATUM (Modules 9–12)

**On this page:** [M9: Regression](#module-9) · [M10: Classification](#module-10) · [M11: Unsupervised learning](#module-11) · [M12: Trees and ensembles](#module-12) · [Shared evaluation rubric](#leakage-safe-rubric)

Choose the module on your route. Its **core outcome and project** define completion; the topic map supplies additional context. Use the [readiness pattern](../guides/readiness-checks.md#how-to-check) to explain, trace, debug and adapt the prerequisite skill before relying on it. Record one next action in the [tracker](../guides/progress-tracker.md#resume).

<details>
<summary>Optional stratum artwork</summary>

<img src="../assets/stratum-3-classical-ml.jpg" alt="Classical machine learning stratum, modules 9 to 12" width="100%">

</details>

> **Reading this page:** each module lists many resources — that is a menu, not a to-do list. Take **one** primary course; see the [resource defaults](../guides/how-to-read-a-module.md#pick-one). Citations like *"Video 1 (05:05)"* are resolved in [sources](../guides/sources.md#citation-key).

> This is the roadmap's synthesis of introductory ML topics. The course links provide primary learning material; topic lists are not a claim that every institution teaches every item in the stated order.

---

<a id="numpy-sprint"></a>
<details>
<summary>Optional refresher map and cross-module implementation sequence</summary>

## 🧮 Before `.fit()`: the 3-step classical ML sequence (v2026.7)

A successful `.fit()` call does not explain the algorithm or validate its assumptions. Build a visual mental map, then a map of the algorithms, then **implement them yourself in NumPy** alongside library comparisons. Distribute the sprint across the modules: logistic regression in M10, K-Means in M11 and the tree in M12. M9 can start with linear regression; implementing all three first is not an entry gate. The time boxes below are adjustable planning examples.

| Step | Time box | What you do | Free resource (pick one) | Done when |
|---|---|---|---|---|
| **1 · Visual maths map** | 2–4 weeks, adjusted to prior knowledge | Matrices as transformations, the chain rule (you need it for backprop), distributions and Bayes' theorem | 3Blue1Brown [*Essence of Linear Algebra*](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) + [*Essence of Calculus*](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) · [StatQuest statistics fundamentals](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF) | You can sketch what `A @ v` does to a vector, and say why a gradient points uphill |
| **2 · Algorithm map** | 2–3 weeks | Classification vs regression; linear vs tree-based vs neural models; overfitting and validation | [ISLP public course videos](https://www.statlearning.com/online-courses) or [StatQuest](https://statquest.org/) | You can say which model family you'd try first on a new tabular problem, and why |
| **3 · Pure NumPy From Scratch Sprint** | 2–4 weeks | Implement **logistic regression**, **K-Means** and a **decision tree** in NumPy, against unit tests | **[`resources/numpy-from-scratch/`](../resources/numpy-from-scratch/README.md#numpy-from-scratch)**: starter files + `pytest` suite, plus optional [Deep-ML](https://www.deep-ml.com/) problems | `pytest -q` passes for all three, and your README explains each place where your version differs from sklearn |

**Why step 3 earns its place:**

- **It turns maths into data flow.** You watch the gradient change the weights, see a point get assigned and a centre move, and see a split chosen. Video 1 (05:00–05:17) describes it as "when you can see the data flow through each step of the algorithm."
- **It supplies interview practice examples.** Explain the algorithm, debug an implementation and justify a numerical choice. The [historical interview-prep discussion](../audit/v2026.7-research-findings.md#interview-prep) motivates these exercises; it does not establish how frequently employers ask them.
- **It's what the module projects build on.** The [M9](#module-9) linear-regression, [M11](#module-11) K-Means and [M12](#module-12) decision-tree projects extend your sprint code. They don't restart it.

> **Rules for the sprint.** Write the algorithm and assumptions before code. Apply the [Foundations AI usage rule](1-foundations.md#ai-usage-rule): independently explain, implement and debug the core you are learning; record assistance and demonstrate a changed case before relying on it. Use `scikit-learn` as a reference comparison, and explain discrepancies before relying on the library result.

</details>

Each module below states its required implementation. Use the refresher above only for gaps; completed maths and algorithm evidence need not be repeated.

<a id="leakage-safe-rubric"></a>
### 📏 Reusable Leakage-Safe Evaluation Rubric (Modules 9–12)

Every project across Modules 9–12 follows this rigorous evaluation discipline, reflecting the [scikit-learn official guide on common pitfalls and data leakage](https://scikit-learn.org/stable/common_pitfalls.html):

1. **Specify the task and freeze evaluation.** Record target, prediction time, population, data licence/version and an untouched test set. Tune on validation folds only; choose thresholds and calibration without using the test set.
2. **Use a baseline matched to the task.** Regression: mean/median or a domain heuristic. Classification: prior-frequency/majority or a business rule. Clustering: one-cluster and resampling stability; supervised PR-AUC is not a clustering metric.
3. **Fit transformations on training folds.** Put learned imputation, scaling, encoding, feature selection and dimensionality reduction in a `Pipeline`/`ColumnTransformer`. Resampling such as SMOTE belongs inside the training fold. A pipeline does not fix a feature measured after the prediction time: audit provenance separately.
4. **Split according to deployment.** Stratify independent classification examples when feasible; group repeated subjects; order temporal data and apply a gap when label windows overlap. Never shuffle future observations into training. Document a combined group/time strategy when both apply.
5. **Choose a primary metric before comparison.** Regression: MAE/RMSE and residuals. Classification: average precision (explicitly name this PR summary), ROC-AUC where meaningful, and a cost-based threshold metric. If probabilities drive decisions, report Brier score/log loss and a calibration plot. State class prevalence and slice sizes; report undefined metrics instead of inventing zeros.
6. **Compare fairly and explain errors.** Use identical folds and a declared tuning/compute budget. Report variability across folds/seeds without calling CV standard deviation a confidence interval. Inspect error slices and worst examples; distinguish association-based explanations from causal drivers. Publish an honest memo even when the baseline wins.

**Practical companion across all four modules:** use the [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
alongside the university/theory route. Its official modules provide browser-based practice for linear
and logistic regression, classification metrics, numerical/categorical data, generalization,
overfitting, embeddings, and real-world ML; it is a practical companion, not a substitute for the
derivations and from-scratch work in M9–M12.

---

<a id="module-9"></a>
## Module 9: Supervised Learning — Regression Family

**Core outcome:** fit and derive linear/Ridge regression, test gradients and stable solvers, and evaluate on untouched data. Principal book: James, Witten, Hastie, Tibshirani and Taylor, **ISLP** (2023; [free author PDF](https://www.statlearning.com/)), chapters 3, 5 and 6. ESL and Bishop supply deeper derivations.

- **Do now:** On a three-row synthetic table, compute one prediction and residual by hand; explain why a target-derived feature would leak.
- **Next:** build the [M9 project](#project-9) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** SVM duals, Gaussian processes and advanced GLM derivations; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Linear regression connects optimization, loss functions, regularization and inference. Understand its assumptions and establish a baseline before increasing model complexity.

* **Strict Prerequisites:** M1, the gradient core of M2, M3 and M5.
* **Recommended Prerequisites:** M6 before coefficient inference; M7 data-validation skills before a real-data project.

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * Framing ML problems (problem class, assumptions, evaluation), baselines, **generalisation (train vs test)**, the ERM principle.
  * Ordinary Least Squares (OLS), closed-form normal equations β̂ = (XᵀX)⁻¹Xᵀy, geometric interpretation as projection onto column space of X, **Ridge Regression** (L2 regularisation, closed form, ties to Tikhonov regularisation), **Lasso** (L1 regularisation, sparsity, coordinate descent solver), **Elastic Net**.
  * Batch GD, SGD, mini-batch SGD, step-size selection, momentum, Nesterov accelerated gradient, convergence analysis for convex quadratic functions.
  * **k-Nearest Neighbours regression** (no training, lazy learning, curse of dimensionality), simple linear regression derivation.
  * Multiple predictors, design matrix, interaction terms, basis expansions (polynomial, piecewise constant, cubic splines, natural cubic splines, smoothing splines).
  * Validation set, **K-fold cross-validation** (standard, stratified, LOOCV, time-series CV with `TimeSeriesSplit`), **information criteria** (AIC, BIC, Mallow's Cp, adjusted R²), **bias-variance decomposition** (formal proof).
  * Coefficient paths, hyperparameter search (grid, random, Bayesian optimisation with Optuna), early stopping as implicit regularisation.
  * **Generalised Linear Models** — exponential family (canonical form, natural parameter, log-partition function, dispersion), link functions (identity, log, logit, probit, complementary log-log), IRLS algorithm.
  * Linear regression in scikit-learn; **gradient descent — batch vs stochastic**; polynomial regression pipeline; regularised linear models.
  * Linear models as projection onto span of features; design of features.
  * **Optional Gaussian-process regression:** kernel functions (squared exponential, Matérn, periodic), marginal likelihood for hyperparameter learning, and a preview of non-parametric Bayesian regression.

</details>

* **Courses and references:**
  * **Primary Course Link:** [ISLP public course videos and Python labs](https://www.statlearning.com/online-courses) — follow the author's public YouTube links for regression, resampling and regularization. [Harvard archived notebooks/slides](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) and [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) are practice companions.
  * **Access Status (5 Nov 2026):** the ISLP author page links public lecture and Python-lab videos. Use those links rather than assuming the associated edX enrollment is free. MIT 6.390's Spring 2026 archive currently reports that the previous semester is inaccessible. Harvard's listed materials do not establish public video access. Google ML Crash Course provides free browser-based instruction; account and regional terms can vary.
  * **Principal reading and further references:**
    * _An Introduction to Statistical Learning with Python_ (ISLP) — Chapters 3, 5, 6.
    * _The Elements of Statistical Learning_ (ESL, 2nd Ed corrected 12th printing) — Chapters 3, 5.
    * _Pattern Recognition and Machine Learning_ (Bishop, 2006) — Chapter 3.
  * **Practical Implementation:** **scikit-learn 1.5+** (`LinearRegression`, `Ridge`, `Lasso`, `ElasticNet`, `KNeighborsRegressor`, `GaussianProcessRegressor`), **statsmodels** for inferential output, **`torch.optim.SGD` / `torch.optim.AdamW`** once you graduate to M15.

<a id="project-9"></a>
* **📦 Module Project (mandatory) — Linear regression from scratch, then honestly evaluated**
  * **Deliverable:** `LinearRegressionScratch` in pure NumPy — a least-squares solution using `np.linalg.lstsq` *and* gradient descent (derive the normal equations but do not invert them in the production path) — plus Ridge; Lasso via coordinate descent or ISTA is optional algorithmic depth. Compare against `sklearn` on a real regression dataset with a proper train/validation/test split and a regularisation path plot.
  * **Definition of done:** (1) `pytest` suite asserting your coefficients match `sklearn`'s to within tolerance on a fixed-seed synthetic problem where you know the true weights; (2) `README.md` with the regularisation path, residual diagnostics, and a statement of which assumptions your data violates; (3) a results memo explaining Ridge shrinkage and the validation trade-off. If you choose the Lasso extension, also explain its zeroed coefficients and their domain plausibility.
  * **Stretch:** Add a bootstrap confidence interval for each coefficient using your [M6](2-statistics-and-data.md#module-6) toolkit and discuss which coefficients you would actually report.
  * *This is the first rung of the [NumPy sequence](#numpy-sprint). Reuse the implementation in the later module comparisons and explain its limitations.*

---

<a id="module-10"></a>
## Module 10: Supervised Learning — Classification & Kernel Methods

**Core outcome:** implement stable logistic regression, compare a classifier baseline, calibrate probabilities and justify a decision threshold. Principal book: **ISLP**, chapters 4 and 9; Bishop PRML chapters 4, 6–7 for optional theory.

- **Do now:** Write a two-by-two confusion matrix for one threshold, then show which error changes when you move it.
- **Next:** build the [M10 project](#project-10) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** kernel proofs, specialized calibration methods and advanced margin theory; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Classification connects probability estimates, decision thresholds and error costs. Logistic regression is the core; kernel methods provide a useful extension when linear boundaries are insufficient.

* **Strict Prerequisites:** M9.
* **Recommended Prerequisites:** M2 Lagrange multipliers and M3 quadratic forms before the optional SVM dual derivation.

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * Sigmoid function σ(z) = 1/(1+e⁻ᶻ), log-odds/logit, **cross-entropy loss** (NLL of Bernoulli), gradient (no closed form), decision boundary (linear), multiclass softmax with categorical cross-entropy, one-vs-rest vs multinomial, class imbalance (oversampling, undersampling, SMOTE, class weights, focal loss).
  * **Perceptron algorithm** (Rosenblatt 1958) — update rule, mistake bound (Novikoff's theorem, proof), linear separability, **Hinge loss and margin boundaries**, regularisation.
  * Feature transformations, **kernel trick** motivation.
  * MLE estimation, Newton-Raphson / IRLS, Wald CIs for odds ratios, ROC curves, AUC, precision/recall/F1/F2, confusion matrix, calibration (Platt scaling, isotonic regression), threshold selection.
  * **Support Vector Machines (SVMs)** — maximum-margin hyperplane derivation, hard-margin primal problem, soft-margin with slack variables ξᵢ, **Lagrangian dual formulation**, KKT conditions, support vectors, **kernel trick** (Mercer's theorem), standard kernels (linear, polynomial, RBF/Gaussian, sigmoid), kernel construction rules, string kernels, graph kernels.
  * Supervised learning via **error minimisation**, **Iterative Reweighted Least Squares (IRLS)** with full derivation, **maximum margin classifier** geometric derivation.
  * The kernel trick formalised, problem formulation as QP, **constrained optimisation and the dual problem**, SVM training algorithm (SMO — Sequential Minimal Optimisation), ν-SVM, one-class SVM for anomaly detection.
  * Treating learning probabilistically — **Bayesian decision theory**, **Bayes-optimal classifier**, likelihood functions and priors, Bayes' theorem applied to supervised learning, **Maximum Likelihood vs Maximum a Posteriori hypotheses** (with proof of equivalence in flat-prior case), reinterpretation of backprop as MLE with squared-error or cross-entropy loss.
  * **Naive Bayes** parameter estimation with Laplace smoothing, statistical laws of language (Zipf's, Heaps'), **statistical tests for classification tasks** (McNemar's test for paired classifier comparison), **cross-validation and test sets**, uncertainty and human agreement (Cohen's κ, Fleiss' κ).
  * Logistic regression in scikit-learn; binary vs multiclass classification via one-vs-rest and softmax; **SVMs** with scikit-learn (`SVC`, `LinearSVC`); kernel selection in practice.
  * VC dimension informal, PAC learning introduction.
  * **Linear Discriminant Analysis (LDA)** — generative classifier, equal class covariance assumption, **Quadratic Discriminant Analysis (QDA)**, Gaussian Naive Bayes as diagonal-covariance QDA.

</details>

* **Courses and references:**
  * **Primary Course Link:** [ISLP public course videos and Python labs](https://www.statlearning.com/online-courses), classification and support-vector-machine chapters. [Cambridge ML&BI](https://www.cl.cam.ac.uk/teaching/2526/MLBayInfer/) supplies additional written theory materials.
  * **Principal reading and further references:**
    * _Pattern Recognition and Machine Learning_ — Bishop — Chapters 4, 6, 7.
    * ISLP — Chapters 4, 9.
    * _Learning with Kernels_ — Schölkopf & Smola — deep dive on SVMs.
  * **Practical Implementation:** **scikit-learn** (`LogisticRegression`, `SVC`, `LinearSVC`, `GaussianNB`, `MultinomialNB`, `LinearDiscriminantAnalysis`, `QuadraticDiscriminantAnalysis`); **`libsvm`** directly for research; **`cvxpy`** to hand-code the SVM dual QP for didactic clarity.

* **🎯 Calibration & Reliability:** In a sufficiently large group of cases assigned `P(y=1 | x) ≈ 0.9`, an observed positive fraction near 0.7 is evidence of overconfident probabilities. Report sampling uncertainty and the population being evaluated; overall classification accuracy is not a calibration measure.
  * **Calibration methods:** [**Platt scaling**](https://en.wikipedia.org/wiki/Platt_scaling) (logistic calibration on held-out scores), **isotonic regression** (non-parametric and more prone to overfitting on small calibration sets; compare by held-out validation), **temperature scaling** (single-parameter scalar on logits; a method evaluated by Guo et al., ICML 2017), **Beta calibration**, **Dirichlet calibration** (multi-class), **histogram binning**.
  * **Metrics:** **Brier score**, **Expected Calibration Error (ECE)**, **Maximum Calibration Error (MCE)**, **reliability diagrams** (calibration curves), **log-loss** decomposition into refinement + calibration.
  * **Practical:** [`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/calibration.html), [`sklearn.calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html), [`netcal`](https://github.com/EFS-OpenSource/calibration-framework) for DL calibration.
  * **Why it matters:** calibration is especially important in risk-sensitive and production systems, including medical, financial, and capacity-planning decisions. Interview emphasis varies by role and employer.

<a id="project-10"></a>
* **📦 Module Project (mandatory) — Churn prediction with a from-scratch core and reproducible interface**
  * **Deliverable:** Two halves. **(a)** `LogisticRegressionScratch` in NumPy using the [practice harness](../resources/numpy-from-scratch/README.md#numpy-from-scratch), verified against `sklearn`. **(b)** A churn-prediction model on a documented, permitted customer-churn dataset — feature engineering, class-imbalance handling, threshold selection driven by a stated cost matrix rather than by accuracy — surfaced in a Streamlit dashboard or reproducible local app that returns a churn probability and association-based feature explanations.
  * **Definition of done:** (1) `pytest` suite over both halves, including a leakage test asserting that no feature derived from the target survives into training; (2) `README.md` with the confusion matrix at your chosen threshold, the cost calculation that justified it, a calibration curve, and either a live URL or exact local/container reproduction command; (3) a results memo stating what the model would cost the business if deployed at your threshold and at the naive 0.5 threshold.
  * **Stretch:** Add SHAP explanations to the dashboard and a monitoring hook that logs the input-feature distribution so you could detect drift.
  * *Archetype source: video 1 (13:10) — the churn-prediction dashboard is named there as a portfolio archetype because it forces business framing, not just model-fitting. A reachable or reproducibly runnable artifact is valuable; public hosting is optional.*

---

<a id="module-11"></a>
## Module 11: Unsupervised Learning, Dimensionality Reduction & Mixture Models

**Core outcome:** implement Lloyd K-Means and PCA, inspect reconstruction/stability and explain what embeddings cannot establish. Principal book: **ISLP**, unsupervised-learning chapter; Murphy PML and Bishop PRML for mixture-model depth.

- **Do now:** Assign four points to two stated centers and perform one Lloyd update; explain what labels would add.
- **Next:** build the [M11 project](#project-11) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** mixture-model inference, metric learning and manifold methods beyond the project comparison; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** The universe is overwhelmingly unlabelled. PCA, Lloyd K-Means and mixture models illustrate different assumptions about unlabelled structure. Evaluate stability and usefulness without inventing labels.

* **Strict Prerequisites:** Module 3 (SVD, eigendecomposition), Module 5 (multivariate Gaussian), Module 9 (MLE).

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * **PCA** derivation three ways — variance maximisation, reconstruction error minimisation, and **SVD of the centred data matrix**; eigenvalue scree plot, Kaiser criterion, parallel analysis; **Advanced Section 3: "Math Foundations of PCA"** — formal proof via Lagrange multipliers; kernel PCA; sparse PCA; probabilistic PCA.
  * **K-means algorithm** (Lloyd's iteration), random initialisation and **K-means++**, within-cluster sum of squares (WCSS), elbow method, silhouette coefficient, gap statistic, **Hierarchical clustering** (agglomerative — single/complete/average/Ward linkage; divisive), dendrograms, cophenetic correlation coefficient, **DBSCAN** (eps, minPts, core vs border vs noise), OPTICS, HDBSCAN (density-based extension), Mean-Shift, Spectral clustering (graph Laplacian eigenvectors).
  * **GMM** as probabilistic clustering, responsibilities γₙₖ, **EM algorithm** for GMMs — E-step computes responsibilities, M-step updates μₖ, Σₖ, πₖ; convergence proof via Jensen's inequality; choosing K via BIC; comparison to K-means (K-means as degenerate GMM).
  * **The k-means algorithm** derivation, **clustering as a maximum likelihood problem** (hard vs soft assignments).
  * **The EM algorithm** — general form (E-step = variational lower bound, M-step = maximise over parameters), application to clustering, application to missing-data problems, **connection to variational inference** (preview of M13).
  * Clustering 1 & 2; Generative models; **Mixture Models and EM algorithm**; Project 4 — Collaborative Filtering via Gaussian Mixtures (**matrix factorisation perspective**).
  * Modern view of unsupervised learning — **autoencoders as non-linear PCA**, bottleneck layer, tied weights, denoising autoencoders, sparse autoencoders.
  * Dimensionality reduction (PCA, Kernel PCA, **ISOMAP**, **Locally Linear Embedding**, **t-SNE** with perplexity tuning, **UMAP** with `n_neighbors`/`min_dist`), matrix estimation (low-rank matrix completion — Netflix prize), feature extraction from unstructured text (topic models — LDA).
  * Unsupervised learning in scikit-learn.
  * **Metric learning**, contrastive learning (SimCLR, MoCo, CLIP training objective), InfoNCE loss, alignment and uniformity criteria.

</details>

* **Courses and references:**
  * **Primary Course Link:** [ISLP public course videos and Python labs](https://www.statlearning.com/online-courses), unsupervised-learning chapter. [Harvard archived notebooks/slides](https://harvard-iacs.github.io/2022-CS109B/) provide additional exercises; public recordings are not assumed.
  * **Principal reading and further references:**
    * ESL — Chapter 14.
    * PRML Bishop — Chapters 9, 12.
    * _Probabilistic Machine Learning: An Introduction_ (Murphy, MIT Press 2022) — chapters 20-21.
  * **Practical Implementation:** **scikit-learn** (`KMeans`, `DBSCAN`, `AgglomerativeClustering`, `GaussianMixture`, `PCA`, `KernelPCA`, `TruncatedSVD`); **`hdbscan`**, **`umap-learn`**, **`openTSNE`**; **`pymc`** for Bayesian GMMs.

<a id="project-11"></a>
* **📦 Module Project (mandatory) — K-Means from scratch + a dimensionality-reduction bake-off**
  * **Deliverable:** `KMeansScratch` in NumPy (random init *and* k-means++ init, with inertia tracking and a proper convergence criterion), plus your own PCA via SVD. Then run a comparison on one high-dimensional real dataset: PCA plus one nonlinear visualization, and K-Means plus one density/mixture alternative, with a defensible cluster-count selection (elbow **and** silhouette **and** a stability check).
  * **Definition of done:** (1) `pytest` suite checking nearest-center labels, non-increasing Lloyd objective and PCA reconstruction/explained-variance invariants; compare sklearn on a separable fixture with matched settings and tolerances, plus a multi-seed comparison of initialization outcomes, without assuming k-means++ must beat random on every fixture; (2) `README.md` with the embedding plots side by side and an explicit warning about what t-SNE/UMAP distances do *not* mean; (3) a results memo naming the clusters and stating whether you believe they are real structure or artefacts.
  * **Stretch:** Cluster on the PCA projection vs the raw features and quantify how much the preprocessing choice changed your conclusions.
  * *Archetype source: video 1 (06:05) — K-Means is one of the three algorithms named for from-scratch implementation.*

---

<a id="module-12"></a>
## Module 12: Ensemble Methods, Tree-Based Learning & Boosting

**Core outcome:** implement a small CART tree, compare bagging and one boosting method, and explain the quality/latency trade-off. Principal book: **ISLP**, chapter 8; ESL for boosting theory.

- **Do now:** Compute the impurity of a hand-worked split before calling a tree estimator.
- **Next:** build the [M12 project](#project-12) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** multiple boosting libraries, stacking and SHAP theory; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** On many tabular-data problems, gradient-boosted trees (XGBoost/LightGBM/CatBoost) are strong baselines and can outperform deep learning, but the result depends on data, metric, and tuning. Compare model families empirically rather than assuming neural networks are always better.

* **Strict Prerequisites:** Modules 9-10 (have solved classification and regression).

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * CART algorithm (Breiman 1984); splitting criteria — **Gini impurity**, **entropy / information gain**, variance reduction for regression; tree growth; pre-pruning (max_depth, min_samples_split) vs post-pruning (cost-complexity pruning α-path); handling of categorical variables; missing-value handling (surrogate splits).
  * Bootstrap aggregation; variance reduction mechanism; out-of-bag (OOB) error estimate as free cross-validation.
  * Feature subsampling (√p for classification, p/3 for regression), **variable importance measures** (Gini importance, permutation importance, SHAP values — previewed), extremely randomised trees (ExtraTrees).
  * **AdaBoost** (weighted training, exponential loss derivation, Friedman-Hastie-Tibshirani statistical view), **Gradient Boosting Machines** (functional gradient descent, learning rate shrinkage, stochastic gradient boosting), **XGBoost** (regularised objective, second-order Taylor expansion of loss, handling missing values, sparse-aware split finding), **LightGBM** (histogram binning, GOSS — Gradient-based One-Side Sampling, EFB — Exclusive Feature Bundling, leaf-wise growth), **CatBoost** (ordered boosting, symmetric trees, native categorical handling).
  * **SHAP** (Shapley values from coalitional game theory, TreeSHAP efficient computation), **LIME** (local surrogate models), **Partial Dependence Plots**, **ICE plots**, permutation-based feature importance, **counterfactual explanations**.
  * **Stacking** (level-0 base learners + level-1 meta-learner), **blending**, **Mixture of Experts** architecture (gating network + expert networks — preview of modern MoE transformers in M18).

</details>

* **Courses and references:**
  * **Primary Course Link:** [ISLP public course videos and Python labs](https://www.statlearning.com/online-courses), tree-based-methods chapter; [Harvard archived notebooks/slides](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) are a written companion.
  * **Principal reading and further references:**
    * ISLP — Chapter 8.
    * ESL — Chapter 10 (boosting), 15 (random forests).
    * XGBoost paper (Chen & Guestrin 2016) — read when selecting the XGBoost extension.
    * _Interpretable Machine Learning_ — Christoph Molnar — [free online, 2024 edition](https://christophm.github.io/interpretable-ml-book/).
  * **Practical Implementation:** **scikit-learn** (`DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`, `HistGradientBoostingClassifier` — a convenient built-in baseline), **XGBoost 2.x**, **LightGBM 4.x**, **CatBoost 1.2+**, **`shap` 0.46+**, **`interpret` (Microsoft InterpretML)**, **`dalex`**.

<a id="project-12"></a>
* **📦 Module Project (mandatory) — Decision tree from scratch, then a boosting bake-off**
  * **Deliverable:** `DecisionTreeScratch` in NumPy — Gini and entropy criteria, recursive splitting, depth and min-samples stopping rules, and a `predict` that walks the tree. Then, on one tabular dataset, run a fair comparison of your tree vs `RandomForest` and one boosting implementation (sklearn histogram boosting is a CPU default; XGBoost/LightGBM/CatBoost are alternatives) with identical folds and a tuned budget per model.
  * **Definition of done:** (1) `pytest` suite covering a pure-node base case, a single-split dataset whose correct split you can compute by hand, and agreement with `sklearn`'s tree on a fixed-seed problem; (2) `README.md` with a leaderboard table (metric ± CV std, fit time, inference latency) — not just the best score; (3) a results memo answering *"would I ship the best model or the second-best, and why"* using the latency and interpretability columns.
  * **Stretch:** Add a permutation-importance and a SHAP comparison, and explain any disagreement between them.
  * *Archetype source: video 1 (06:05) — decision trees are the third named from-scratch implementation.*

---

[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟨 Statistics & Data (M6–M8b)](2-statistics-and-data.md) · [🟦 Probabilistic ML (M13–M14) →](4-probabilistic-ml.md)
