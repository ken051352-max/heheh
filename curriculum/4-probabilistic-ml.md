[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟧 Classical ML (M9–M12)](3-classical-ml.md) · [🟪 Deep Learning (M15–M17) →](5-deep-learning.md)

---

# 🟦 PROBABILISTIC & BAYESIAN STRATUM (Modules 13–14)

**On this page:** [M13: Bayesian modelling](#module-13) · [M14: Forecasting](#module-14)

Choose the module on your route. Its **core outcome and project** define completion; the topic map supplies additional context. Use the [readiness pattern](../guides/readiness-checks.md#how-to-check) to explain, trace, debug and adapt the prerequisite skill before relying on it. Record one next action in the [tracker](../guides/progress-tracker.md#resume).

<details>
<summary>Optional stratum artwork</summary>

<img src="../assets/stratum-4-bayesian.jpg" alt="Probabilistic and Bayesian stratum, modules 13 to 14" width="100%">

</details>

> **Reading this page:** each module lists many resources — that is a menu, not a to-do list. Take **one** primary course; see the [resource defaults](../guides/how-to-read-a-module.md#pick-one). Citations like *"Video 1 (05:05)"* are resolved in [sources](../guides/sources.md#citation-key).

---

<a id="module-13"></a>
## Module 13: Bayesian Inference, Graphical Models & MCMC

**Core outcome:** build a generative model, perform prior/posterior predictive checks, diagnose sampling and communicate sensitivity. Principal recommended book: McElreath, **Statistical Rethinking**, second edition (paid; [free author lectures/code](https://github.com/rmcelreath/stat_rethinking_2024)). Murphy **Probabilistic Machine Learning: Advanced Topics** (MIT Press 2023; [author resources](https://probml.github.io/pml-book/)) is the advanced reference. Use PyMC 5.x first; NumPyro and Stan are alternatives.

- **Do now:** Specify a binary outcome, prior and likelihood; compute the Beta-Binomial posterior for a tiny count example before sampling.
- **Next:** build the [M13 project](#project-13) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** graphical-model algorithms, sequential Monte Carlo and variational inference; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Bayesian modeling makes assumptions and uncertainty explicit. Build the data-generating story, inspect prior predictions and diagnose the posterior before trusting a decision.

* **Strict Prerequisites:** M5 probability and M6 inference; M3 linear algebra for multivariate models.
* **Recommended Prerequisites:** M9 regression for the book’s modeling chapters; M11 EM before variational/mixture-model extensions.

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * **Philosophical basis of Bayesianism** — subjective probability, Cox's theorem (probability as extension of logic), Dutch book argument. Prior × Likelihood ∝ Posterior. Conjugate prior families (Beta-Binomial, Gamma-Poisson, Normal-Normal, Dirichlet-Multinomial, Normal-Inverse-Gamma, Normal-Inverse-Wishart).
  * **Posterior predictive distribution**, credible intervals vs confidence intervals (conceptual distinction), marginal likelihood (evidence), Bayes factors for model comparison.
  * **Hierarchical (multi-level) Bayesian models** — partial pooling, shrinkage, James-Stein estimator, empirical Bayes, Gibbs sampling introduction.
  * **Markov Chain Monte Carlo (MCMC)** — detailed balance condition, **Metropolis-Hastings algorithm** with proposal distributions and acceptance probability, **Gibbs sampling** (when conditionals are tractable), Hamiltonian Monte Carlo (HMC) preview.
  * **Variational Inference** — ELBO (Evidence Lower Bound) derivation, mean-field approximation, coordinate ascent VI, **stochastic VI**, normalising flows preview, **reparameterisation trick** (preview of VAEs in M16).
  * **Sequential Monte Carlo** — bootstrap filter, importance sampling, resampling (systematic, residual, stratified), particle degeneracy, effective sample size, auxiliary particle filter.
  * **Directed graphical models (Bayesian networks)** — representing uncertain knowledge as DAGs, joint distribution factorisation, **conditional independence** (d-separation, Markov blanket), **exact inference** (variable elimination, junction tree algorithm / message passing, belief propagation for trees).
  * **Markov Random Fields (undirected graphical models)** — Gibbs distributions, potential functions, Hammersley-Clifford theorem, Ising model, **approximate inference**, **Markov chain Monte Carlo methods** (full MH + Gibbs treatment).
  * **The Bayesian approach to neural networks** — Laplace approximation (Gaussian at MAP), Bayesian backpropagation (MacKay), MC dropout as approximate Bayesian inference.
  * Incorporating prior knowledge, sampling from complex distributions, Bayes rule as basis of all inference, selecting priors (Gaussian → ridge; Laplace → lasso; Dirichlet-process for non-parametric Bayes), **Gibbs sampling derivation**, **Metropolis-Hastings with full proof of detailed balance**.
  * **Maximum-likelihood vs Bayesian inference** — strengths and weaknesses of both; **belief propagation** algorithm.

</details>

* **Courses and references:**
  * **Primary Course Link:** [McElreath Statistical Rethinking — free lecture recordings and code](https://github.com/rmcelreath/stat_rethinking_2024) · [Harvard CS109B archived materials](https://harvard-iacs.github.io/2022-CS109B/) · [Cambridge ML and Bayesian Inference](https://www.cl.cam.ac.uk/teaching/2526/MLBayInfer/) (theory depth). The author course uses R/Stan; adapt computations to current PyMC rather than copying old PyMC3 conversions unchanged.
  * **Principal reading and further references:**
    * _Probabilistic Machine Learning: Advanced Topics_ (Kevin Murphy, **MIT Press 2023**) — Chapters 1-12 (advanced reference; select relevant chapters).
    * _Bayesian Data Analysis_ (**3rd Edition**) — Gelman, Carlin, Stern, Dunson, Vehtari, Rubin (BDA3).
    * _Pattern Recognition and Machine Learning_ — Bishop — Chapters 8 (graphical models), 10 (VI), 11 (MCMC).
    * _Bayesian Reasoning and Machine Learning_ — David Barber — [free PDF](http://www.cs.ucl.ac.uk/staff/D.Barber/brml/) (explicitly listed in Cambridge ML&BI reading list).
  * **Practical Implementation:** **PyMC 5.x** (with PyTensor backend), **NumPyro** (JAX-native alternative; benchmark compilation and sampling separately on your model), **Stan** via `cmdstanpy`, **`arviz`** for posterior diagnostics (R̂, ESS, trace plots, posterior predictive checks).

**Book selection evidence:** [Aki Vehtari’s Aalto BDA course](https://avehtari.github.io/BDA_course_Aalto/index.html) recommends McElreath’s second edition as an accessible entry and identifies its limits relative to BDA3; [Jim Albert’s published review](https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1806761) supports its applied-modeling role. These support this choice, not a claim of universal consensus.

**Diagnostic reference:** [Stan's convergence guidance](https://mc-stan.org/learn-stan/diagnostics-warnings.html) and ArviZ explain why R-hat alone is insufficient. Choose ESS/MCSE targets for the quantity being reported; a fixed seed does not guarantee convergence.

<a id="project-13"></a>
* **📦 Module Project (mandatory) — Bayesian A/B test, end to end**
  * **Deliverable:** A full Bayesian analysis of a real or realistically-simulated experiment in PyMC or NumPyro: state the prior and defend it, fit the posterior, run convergence diagnostics (R-hat, ESS, divergences, trace and rank plots), do prior and posterior predictive checks, and report a decision — including the probability that B beats A by more than a stated business-relevant margin.
  * **Definition of done:** (1) deterministic checks against an analytic Beta-Binomial case and a sampling diagnostic report: multiple chains, rank-normalized split R-hat < 1.01, bulk/tail ESS, Monte Carlo SE and zero unresolved post-warmup divergences; explain any warning and rerun a diagnosed model rather than repeatedly changing seeds to obtain a pass; (2) `README.md` with the posterior plots, the prior-sensitivity analysis (re-run under at least two other defensible priors), and the decision rule; (3) a results memo contrasting your Bayesian conclusion with the frequentist p-value from your [M6](2-statistics-and-data.md#module-6) toolkit on the same data — and explaining precisely what each one does and does not claim.
  * **Stretch:** Extend to a hierarchical model across segments and show partial pooling shrinking the noisy small-segment estimates.
  * **Fast-lane note:** This module is where the [intuition-first shortcut runs out](1-foundations.md#module-5). If you are here, you need the probability spine.

---

<a id="module-14"></a>
## Module 14: Sequence Modelling — HMMs, Kalman Filters & Time Series

**Core outcome:** produce a leakage-safe rolling-origin forecast with a baseline, uncertainty report and a decision memo. Principal book: Hyndman and Athanasopoulos, **Forecasting: Principles and Practice**, third edition (free). Its examples use R; implement the same statistical workflow in Python if preferred. HMMs, Kalman filters and neural forecasting are optional branches after the core.

- **Do now:** Draw one prediction origin and its available history; produce a naive forecast without touching later observations.
- **Next:** build the [M14 project](#project-14) with its tests and results memo. Use the free lecture default and selected principal reading below.
- **Later depth:** HMMs, Kalman filters, neural forecasting and causal interventions; choose these only for a specific gap or specialization.

* **The Tutor's "Why":** Forecasts must use information available at the prediction time. Rolling-origin evaluation exposes leakage, changing dynamics and horizon-dependent uncertainty; state-space models provide a later unifying framework.

* **Strict Prerequisites:** M5, M7 and M9 for the forecasting core.
* **Recommended Prerequisites:** M13 before Bayesian state-space/message-passing extensions; M15 before neural forecasting.

<details>
<summary>Full topic map: core context and later depth</summary>

The core outcome, practical contracts and project remain the required route. This breadth map is not a checklist of extra prerequisites.

* **Topic map (roadmap synthesis):**
  * **Hidden Markov Models (HMM)** — model definition (hidden state chain + observation emissions), assumptions (Markov property on hidden chain, observation independence given state), the three canonical problems (Rabiner 1989):
    1. **Evaluation** — P(observations | model) via **Forward algorithm**.
    2. **Decoding** — most likely hidden sequence via **Viterbi algorithm** (with full dynamic-programming derivation).
    3. **Learning** — parameter estimation via **Baum-Welch / Forward-Backward** (EM for HMMs).
    * Application: **predicting protein interactions with a cell membrane** (Cambridge's specific biological application).
  * Bernoulli process, Poisson process, **hidden random processes** (preview of state-space models).
  * **Kalman filter** implementation — state-space model for linear Gaussian systems, prediction step and update step, Rauch-Tung-Striebel smoother, **extended Kalman filter (EKF)** for nonlinear systems, **unscented Kalman filter (UKF)**, connection to Bayesian belief update.
  * Time series basics — trend, seasonality, cyclicity, stationarity (strong vs weak/covariance stationarity), ACF/PACF, white noise tests (Ljung-Box); ARMA models; **ARIMA** and **SARIMA** (Box-Jenkins methodology); Vector Autoregression (VAR); Granger causality; cointegration and Engle-Granger two-step; **ARCH/GARCH** for volatility; state-space formulation; Kalman filter as linear-Gaussian HMM; structural time-series models (Harvey BSM); **prophet** (a decomposable forecasting model); **DeepAR**, **Temporal Fusion Transformers** (optional neural forecasting); **intervention analysis** (difference-in-differences, interrupted time series, synthetic control); regression discontinuity; instrumental variables for causal inference.
  * **RNN for sequence modelling** (connects to M15).
  * **Long Short-Term Memory (LSTM)** — gate equations (input, forget, output gates), cell state, vanishing gradient solution; **Gated Recurrent Unit (GRU)** — update and reset gates.

</details>

* **Courses and references:**
  * **Primary Course Link:** [Hyndman's FPP3 video lectures and playlist](https://robjhyndman.com/hyndsight/fpp3_videos.html), paired with [Forecasting: Principles and Practice, third edition](https://otexts.com/fpp3/). Videos accompany most book sections; the text and examples fill the gaps. [Cambridge MLRD](https://www.cl.cam.ac.uk/teaching/2324/MLRD/) is written material for the optional HMM extension.
  * **Principal reading and further references:**
    * _Forecasting: Principles and Practice_ (**3rd Edition**) — Rob J. Hyndman and George Athanasopoulos — [free online](https://otexts.com/fpp3/).
    * _Time Series Analysis_ — James Hamilton — classical econometric reference.
    * Rabiner, "A Tutorial on Hidden Markov Models" (IEEE 1989) — historical reading for the optional HMM extension.
    * Bishop PRML — Chapter 13 (sequential data).
  * **Practical Implementation:** **`statsmodels.tsa`** (ARIMA, SARIMAX, VAR, state-space), **`pmdarima`** (auto-ARIMA), **`prophet` 1.1+**, **`hmmlearn`**, **`pykalman`**, **`filterpy`** for Kalman variants, **`darts`** (one optional forecasting library), **`sktime` 0.30+**, **`neuralforecast`** (Nixtla) for modern deep TS.


**Uncertainty and hierarchy:** compare empirical interval coverage and width by forecast horizon, not just overall coverage. Calibrate using residuals available strictly before each origin. Standard split-conformal marginal coverage relies on exchangeability; arbitrary dependent/drifting time series do not inherit that guarantee. [Gibbs and Candès ACI](https://proceedings.neurips.cc/paper_files/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf) targets long-run coverage frequency under its update rule, not conditional coverage for every horizon or subgroup. Discuss potentially uninformative intervals. For hierarchical reconciliation, estimate reconciliation inputs on training data and evaluate accuracy and coherence separately.

**Forecasting workflow:** lock frequency, target availability, prediction origin and horizon; distinguish missing periods from zeros; build lags inside each training window; fit transforms only on training history; tune with rolling origins and keep a final chronological holdout. External regressors must be available at forecast time. Granger predictability is not intervention causality.

<a id="project-14"></a>
* **📦 Module Project (mandatory) — A time-series investigation with honest forecasting**
  * **Deliverable:** A dashboard or reproducible local app over a real time series (equities, energy demand, or web traffic) that shows the history, a forecast with prediction intervals, and — critically — a **backtest** using rolling-origin cross-validation. Use a naive baseline and seasonal-naive where seasonality is plausible, then compare one ARIMA/ETS model. Record any series where seasonal-naive is inapplicable rather than manufacturing seasonality.
  * **Definition of done:** (1) `pytest` suite including a test that asserts your backtest split never leaks future data into training; (2) `README.md` with MAE/MASE (document the scaling denominator), interval coverage/width and results by horizon for every baseline/model, and either a live URL or exact local/container reproduction command; (3) a results memo stating plainly whether your model beat the applicable naive baseline, including seasonal-naive when justified.
  * **Stretch:** compare bottom-up vs reconciled forecasts on a hierarchy, checking that child forecasts sum to their parent; or evaluate a probabilistic/foundation model with the same rolling origins and compute budget.
  * *Archetype source: video 1 (13:55) — the stock dashboard, with the backtest and baseline requirements added because the archetype is otherwise the easiest portfolio project to fake.*

---

[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟧 Classical ML (M9–M12)](3-classical-ml.md) · [🟪 Deep Learning (M15–M17) →](5-deep-learning.md)
