[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [🟨 Statistics & Data (M6–M8b) →](2-statistics-and-data.md)

---

<a id="new-here"></a>
> **🌱 Start here if you're new**
>
> 1. New to Python? **[Open Week 0](../guides/week-0.md#week-0).** Seven days, in your browser, nothing to install.
> 2. Then follow the [first 30 days](../guides/first-30-days.md#first-30-days). That is the gentle start of Module 1.
> 3. You don't need anything else on this page yet. No diagnostic, no proofs, no tooling.
> 4. The maths placement in Week 2 only helps you pick resources. It never blocks you.
> 5. The rest of this page is reference for later. It will wait for you.

# 🟩 FOUNDATION STRATUM — Modules 0–5

<img src="../assets/stratum-1-foundations.jpg" alt="Foundation stratum, modules 0 to 5" width="100%">

> **Reading this page:** each module lists many resources — that is a menu, not a to-do list. Take **one** primary course; see the [Pick-One table](../guides/how-to-read-a-module.md#pick-one). Citations like *"Video 1 (05:05)"* are resolved in [sources](../guides/sources.md#citation-key).

> These six modules build the maths and programming base for everything later. Follow the **core outcome** in each module; extended topic lists are optional depth; one principal book is recommended by quality, with its access/cost labeled. The [learning contract](README.md#learning-contract) defines reviewable evidence and lets you reuse an evolving project. A local or privately shared artifact is sufficient.

<details>
<summary><strong>Advanced / later:</strong> why the original authors call this base "non-negotiable"</summary>

> Mathematical and programming foundations support later work: eigenvalues help explain PCA, the chain rule supports backpropagation, and quantifiers clarify proofs. Follow the prerequisites of your chosen route and revisit a specific gap when it affects your work.

</details>

---

<a id="math-diagnostic"></a>
## 🩺 Maths placement (optional, never a gate)

**For beginners:** take this once in [Week 2 of your first 30 days](../guides/first-30-days.md#week-2). It tells you which free resources fit you. **It never blocks Module 1**, and nobody "fails" it.

<a id="math-placement-step-1"></a>
### Step 1 — Take one free placement check (30–45 min)

| Who | Placement check | What it covers |
|---|---|---|
| **Everyone** | [Khan Academy Precalculus course challenge](https://www.khanacademy.org/math/precalculus/test/x9e81a4f98389efdf:course-challenge) (free account, 30 questions, about 30–45 min) | Functions, trigonometry, complex numbers, vectors, matrices, series |
| **Optional, if that felt easy** | Try one practice exam from [MIT 18.01 Single Variable Calculus — exams](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/exams/) (MIT OCW, free; solutions included) | Limits, derivatives, integrals |

> **Honesty note.** Earlier versions promised a unified 15-question diagnostic. It was never written,
> and two legacy links in that proposal—the MIT 18.01A exam and Velleman §1.5 exercise link—are
> retired/broken. The table above replaces them with checks that exist and are free today. The original
> six-strand table is kept below only as provenance.

<a id="math-placement-step-2"></a>
### Step 2 — Use your result to pick resources (never to stop)

Keep going with [Module 1](#module-1) whatever you score. Then add **one** of these, at about 15–30 min a day:

| Your Khan course-challenge result | Add this alongside Python |
|---|---|
| **Many questions felt unfamiliar** | The Khan units you missed (the course challenge shows them). Then the [beginner maths track](#beginner-math-track). |
| **Mixed** | The [beginner maths track](#beginner-math-track), starting with 3Blue1Brown. Revisit missed Khan units when your college course reaches them. |
| **Most questions felt easy** | The [beginner maths track](#beginner-math-track) at a faster pace, plus an MIT 18.01 practice exam if you like a stretch. |

Your college maths course is still your main maths course. These resources sit beside it.

<a id="beginner-math-track"></a>
### 🌱 Beginner maths track (free, alongside Python)

A gentle, visual route that touches code early. It runs alongside your college maths, not instead of it.

| Order | Resource | Time | Why |
|---|---|---|---|
| 1 | 3Blue1Brown, [*Essence of Linear Algebra*](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | ≈ 3 h of video | Pictures first: vectors, matrices, transformations |
| 2 | 3Blue1Brown, [*Essence of Calculus*](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) | ≈ 3 h of video | Derivatives and the chain rule as pictures |
| 3 | [Khan Academy Precalculus](https://www.khanacademy.org/math/precalculus) | Self-paced | Practise algebra, functions and trigonometry before the university calculus route |
| Companion | Your college course, or MIT [18.01](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/) and [18.06](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) on OCW | — | Full university depth when you are ready for [Module 2](#module-2) and [Module 3](#module-3) |
| Proof habit | [*Book of Proof*](https://richardhammack.github.io/BookOfProof/), chapters 1–4 | 15 min/day | Sets, logic and the first proof techniques ([Module 0b](#module-0), reduced) |

> **Access:** use the free Khan, 3Blue1Brown and MIT OCW materials above. Recommended books may be paid; no paid lecture platform or subscription is part of this route.

<details>
<summary><strong>Archival / Non-operational:</strong> historical six-strand diagnostic reference (superseded)</summary>

> **Non-operational archival notice:** The text below is preserved strictly for historical reference and provenance. The promised unified 15-question diagnostic exam was never written, two of its external links (MIT 18.01A exam and Velleman §1.5) are retired/broken (see [`audit/VERIFICATION.md`](../audit/VERIFICATION.md#v2026-6-first-30-days)), and the 70% thresholds below are unvalidated historical cutoffs. **Do not use this table as a placement gate.** Use the active, free, non-gating [maths placement workflow](#math-diagnostic) above instead.

## 🩺 (Historical) Math-Foundations Diagnostic & Remediation Reference

*(Archival reference only — non-operational)*

| # | Strand | Diagnostic instrument | Historical Pass bar | Historical Remediation Note |
|---|---|---|---|---|
| 1 | **Pre-calculus & algebra** | [Khan Academy Precalculus course challenge](https://www.khanacademy.org/math/precalculus/test/x9e81a4f98389efdf:course-challenge) | 70 % (archival) | Module **0a** (Khan Academy Pre-Calc) |
| 2 | **Trigonometry & complex numbers** | [Paul's Online Trig diagnostic](https://tutorial.math.lamar.edu/) | 7/10 (archival) | Module **0a** (Khan Academy Trig + Euler's formula) |
| 3 | **Proof writing & logic** | [Velleman *How To Prove It* §1.5 exercises](https://www.cambridge.org/highereducation/books/how-to-prove-it/6D2965D625C6836CD4A785A2C843B3DA) | 4/5 (archival) | Module **0b** (Hammack *Book of Proof*) |
| 4 | **Single-variable calculus** | [MIT 18.01 exams page (use the final)](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/exams/) | 70 % (archival) | Module **2** (full) |
| 5 | **Linear algebra (computational)** | [MIT 18.06 Quiz 1](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/exams/) | 70 % (archival) | Module **3** (full) |
| 6 | **Probability sense** | [Harvard Stat 110 Practice Strategic Practice 1–3](https://stat110.hsites.harvard.edu/) | 70 % (archival) | Module **5** (full) |

*(Historical note: The score-based gating rules originally drafted here were retired in favor of the non-gating placement workflow above. No learner is blocked from starting Python or foundational math.)*

</details>

<details>
<summary><strong>Advanced / later:</strong> the Math Maturity Operating Manual (seven habits, including optional Lean)</summary>

<a id="math-maturity-manual"></a>
### Step 3 — Adopt the **Math Maturity Operating Manual**

Practise these **seven study habits**, selected for this curriculum:

1. **Quantifier discipline** — when you read "for every / there exists", you can write it as `∀ / ∃` and negate it correctly.
2. **Definition-unfolding** — given a theorem, you can rewrite each term to its primitive definition before reasoning.
3. **Counter-example reflex** — when you doubt a claim, you immediately try `n=0`, `n=1`, the empty set, the singleton, and the constant function.
4. **Proof-template recall** — induction, contradiction, contrapositive, direct, construction, pigeonhole — each as a *template* you can fill in.
5. **Notation hygiene** — distinguish `=` (equal), `:=` (defined-as), `≡` (congruent / identical), `≈` (approximately), `∼` (asymptotic), `∝` (proportional).
6. **Computational checks** — use **SymPy** or **NumPy** to test examples and find counterexamples; numerical agreement is not a proof.
7. **Lean / proof-assistant exposure** — optionally try a chapter of [Velleman's *How To Prove It With Lean*](https://djvelleman.github.io/HTPIwL/) to make definitions and proof steps explicit.

> These are teaching recommendations, not a claim that a university mandates this exact checklist.

</details>

---

<a id="module-0"></a>
## Module 0: Mathematical Maturity Bridge — Pre-Calculus, Logic & Proof

**Recommended principal reading:** Richard Hammack, **Book of Proof**, third edition (free author PDF and paid print): definitions, direct/contradiction proofs and induction.

**Core outcome:** translate quantified statements, give a counterexample, and write a direct, contradiction and induction proof with assumptions. Keep a proof notebook. This bridge remains optional preparation, never a gate for Python.

> **Status:** Recommended, never a gate. Beginners: do *Book of Proof* ch. 1–4 at 15 min/day alongside college maths (see the [beginner maths track](#beginner-math-track)). The full module is for later.

<details>
<summary><strong>Archival / Non-operational:</strong> historical status line</summary>

> *(Archival / non-operational)* Originally drafted: Optional only if you scored > 70 % on every diagnostic above. Otherwise: mandatory. *(Historical text preserved for record; current status is non-gating as stated above.)*

</details>

* **The Tutor's "Why":** University maths is built on definitions and proofs, and most courses assume you already made that jump from school maths. This module is a free, gentle bridge across it.

  <details>
  <summary><strong>Advanced / later:</strong> the original rationale</summary>

  **The Tutor's "Why":** Definitions, logic and proof techniques support later probability and ML reading. This bridge introduces those habits; it supplements a full proof course rather than claiming equivalent depth.

  </details>

* **Strict Prerequisites:** Working knowledge of high-school algebra (solve linear and quadratic equations).

### Sub-module 0a — Pre-Calculus & Trigonometry Refresher (≈ 2–4 weeks)

* **Topic map (core plus optional depth; roadmap synthesis):**
  * **Numbers:** ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ; absolute value as distance; intervals; surds and rationalising.
  * **Algebra:** factorisation (difference of squares, sum/difference of cubes), polynomial long division, partial fractions, exponent and log laws, change-of-base formula, **completing the square** (useful in Gaussian and regression algebra).
  * **Functions:** domain/range, composition, invertibility, even/odd, increasing/decreasing, piecewise, absolute value, floor/ceiling.
  * **Conic sections:** circle, ellipse, parabola, hyperbola — equations and parametrisations (you'll see them again in Gaussians and SVMs).
  * **Trigonometry:** unit circle, radian measure, six trig functions, identities (Pythagorean, sum/difference, double-angle, half-angle, product-to-sum), inverse trig, polar coordinates.
  * **Complex numbers:** Cartesian and polar form, **Euler's formula `eⁱᶿ = cos θ + i sin θ`** (the bridge to Fourier transforms in M3), De Moivre's theorem, roots of unity.
  * **Sequences & series:** arithmetic and geometric, sum formulas (you will re-derive these in MGFs in M5).
  * **Limits — informal:** ε-δ intuition, one-sided limits, infinite limits, limits at infinity.

* **Courses and references:**
  * **Primary (free):** [Khan Academy Precalculus](https://www.khanacademy.org/math/precalculus) — 10 units, ≈ 40 hours, includes mastery quizzes.
  * **Alternative (free, MIT-quality):** [MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — self-paced OCW Scholar course (18.01A was retired from OCW; replaced v2026.7), ideal if you have 6+ weeks.
  * **Reading:** Stewart *Calculus, Early Transcendentals* (9th ed.) — Appendix A (numbers), Appendix B (coordinate geometry), Appendix C (graphs), §1.1–§1.5 (functions and models).
  * **Computational verification:** use **SymPy** to check examples and identities where useful (e.g., `sympy.simplify(sin(x)**2 + cos(x)**2 - 1)`).

### Sub-module 0b — Logic, Proof & Mathematical Vernacular (≈ 4–6 weeks · CORE)

* **Topic map (core plus optional depth; roadmap synthesis):**
  * **Propositional logic:** truth tables, conjunction `∧`, disjunction `∨`, negation `¬`, implication `⟹`, biconditional `⟺`, **converse / contrapositive / inverse** (and which are logically equivalent).
  * **Predicate logic:** universal `∀`, existential `∃`, **negating quantified statements** (`¬∀x P(x) ≡ ∃x ¬P(x)`); practise translating the negation into words and checking examples.
  * **Sets:** ∅, ∈, ⊆, ⊊, ∪, ∩, complement, Cartesian product, power set, Russell's paradox (and why ZFC patches it).
  * **Functions formally:** as relations satisfying functional dependence; injection, surjection, bijection; image and pre-image; composition; inverse function theorem (statement only).
  * **Relations:** reflexive, symmetric, transitive, equivalence relations, partitions, partial and total orders.
  * **Cardinality:** finite, countably infinite (ℕ ∼ ℤ ∼ ℚ), uncountable (ℝ via Cantor's diagonal); pigeonhole as a corollary.
  * **Proof techniques (with at least 3 worked examples each):**
    1. **Direct proof** — e.g., sum of two evens is even.
    2. **Proof by contradiction** — e.g., √2 is irrational; there are infinitely many primes.
    3. **Proof by contrapositive** — e.g., if `n²` is even then `n` is even.
    4. **Proof by mathematical induction** (weak and strong) — e.g., `Σk=1ⁿ k = n(n+1)/2`; well-ordering principle.
    5. **Proof by construction** — e.g., explicitly construct a bijection ℕ → ℤ.
    6. **Proof by cases** — e.g., triangle inequality.
    7. **Pigeonhole principle** — e.g., among any 13 people, two share a birth-month.
  * **Number theory primer:** divisibility, gcd, Euclidean algorithm (with extended version), Bezout's identity, modular arithmetic, Fermat's little theorem, Chinese Remainder Theorem (used in cryptography and hashing).
  * **Combinatorial identities:** Pascal's rule, hockey-stick identity, Vandermonde's identity (use story proofs or algebra to verify one identity).
  * <details><summary><strong>Advanced / later:</strong> optional Lean 4 first contact</summary>

    **(Optional) Lean 4 first contact:** prove `∀ n : ℕ, n + 0 = n` interactively. *Optional practice in explicit definitions and proof steps.*

    </details>

* **Courses and references:**
  * **Primary text (free):** [_Book of Proof_ (Richard Hammack, **3rd Edition**)](https://richardhammack.github.io/BookOfProof/) — chapters 1–10. The author provides the complete text and identifies its American Institute of Mathematics Open Textbook Initiative approval.
  * **Companion text:** [_How to Prove It: A Structured Approach_ (Velleman, **3rd Edition, Cambridge 2019**)](https://www.cambridge.org/highereducation/books/how-to-prove-it/6D2965D625C6836CD4A785A2C843B3DA) — chapters 1–6 + the new **[*How to Prove It With Lean* (Velleman, 2024)](https://djvelleman.github.io/HTPIwL/)** companion (free, browser-based).
  * **Discrete-math companion:** [_Mathematics for Computer Science_ (Lehman, Leighton, Meyer — MIT 6.042J, **free course textbook**)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook/) — chapters 1–5 (Proofs, Induction, Number Theory).
  * **Lecture notes and exercises:** [Stanford CS103 Mathematical Foundations of Computing](https://web.stanford.edu/class/cs103/) — public written materials; video availability is not assumed.
  * **Practical implementation:** **SymPy 1.13+** for symbolic verification; **Lean 4 + Mathlib** (optional) — `lean4-web` runs in browser, no install needed.

* **Outcome:** Restate the assumptions and conclusion of an introductory theorem and choose a plausible proof method. Use a counterexample to explain why a missing assumption matters.

* **Suggested Pace:** Beginners: *Book of Proof* ch. 1–4 at **15 min/day** alongside college maths. Full module later: 6 weeks at 10 hrs/week, or 12 weeks at 5 hrs/week. Hammack provides 600+ exercises with hints; **about 200 is a recommended target, not a gate** before [Module 2](#module-2).

  <details>
  <summary><strong>Advanced / later:</strong> the original pace note</summary>

  **Suggested Pace:** 60 hours can be scheduled as six weeks at ten hours/week or twelve at five. Treat this as a planning example. Select exercises that expose gaps in definitions and proof methods; a fixed exercise count is not the module outcome.

  </details>

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The route:** Skip Module 0 entirely. Go straight to [M1](#module-1), and pick up mathematical vocabulary as it appears via [StatQuest](https://statquest.org/) and the [Manga Guides](../resources/books.md#practitioner-shelf). Return here only if you later hit the wall described below.
>
> **The argument for it:** Video 3 (04:47) — *"You need intuition, not derivation skills. Get the concepts down and then move forward."* Video 1 (00:44–01:09) reports that months spent on manual derivations "took years longer than it needed to" and did not yield "great intuition for why models behave the way they do in practice."
>
> **What you give up — stated plainly:** The shortened route defers formal proof practice. Prior equivalent knowledge counts; revisit definitions, quantifiers and proof methods whenever you cannot explain an assumption or conclusion.
>
> **Come back when:** you enter [M13](4-probabilistic-ml.md#module-13) (Bayesian derivations), any research-track work, or you find yourself unable to tell whether a paper's claim is actually supported. Module 0 is 60 hours; it does not expire.

---

<a id="module-1"></a>
## Module 1: Programming Foundations & Computational Thinking

**Recommended principal reading:** Eric Matthes, **Python Crash Course**, third edition (No Starch, paid): a structured beginner reference. Luciano Ramalho, **Fluent Python**, second edition (O’Reilly, paid), is later language depth. No purchase is needed for Week 0 or CS50P lectures.

**Core outcome:** complete CS50P or equivalent outcomes, the starter milestone, and the tested Weather CLI. Pydantic boundary validation follows ordinary Python types; async and streaming are later extensions. Choose one main course and use the book shelf for optional depth.

* **The Tutor's "Why":** This roadmap uses Python for data analysis, numerical experiments and AI applications. Turn a small specification into a program you can explain, test and reproduce.

* **🌱 New to programming?** Do [Week 0](../guides/week-0.md#week-0) and the [first 30 days](../guides/first-30-days.md#first-30-days) first. They cover CS50P weeks 0–3 and your [starter project](#m1-starter-project).

  <details>
  <summary><strong>Advanced / later:</strong> the original rationale</summary>

  **The Tutor's "Why":** Python connects the exercises in this roadmap. Other languages remain useful; the goal here is reliable programming practice, not a claim about every industry role.

  </details>

* **Strict Prerequisites:** None beyond basic literacy and a web browser for the beginner route. Week 0 runs in Scrimba, and CS50P provides VS Code in the browser at [cs50.dev](https://cs50.dev/). A local VS Code install and high-school algebra are useful later, but neither gates starting Python.

* **Topic map (core plus optional depth; roadmap synthesis):**
  * Functions, variables, types (int/float/str), `print`, formatted strings, conditionals, boolean expressions.
  * Conditionals, `match` statement, flow control, truthy/falsy semantics.
  * Loops (`for`, `while`), iterables, `break`/`continue`, `enumerate`, `zip`.
  * Exceptions, `try/except/else/finally`, raising custom exceptions, `assert`.
  * Libraries, `import`, `pip`, standard library tour (`random`, `statistics`, `sys`, `pathlib`).
  * Unit testing, `pytest`, test-driven development, fixtures, parametrise.
  * File I/O, CSV, JSON, binary files, context managers (`with`), PIL/Pillow basics.
  * Regular expressions, `re.search/match/sub/findall`, character classes, anchors, lookaheads.
  * Object-Oriented Programming: classes, `__init__`, attributes, methods, `@classmethod`, `@staticmethod`, `@property`, inheritance, `super()`, dunder methods (`__str__`, `__repr__`, `__eq__`).
  * **Python extensions after the course:** comprehensions, generators, decorators, `*args`/`**kwargs` and typing; consult the official Python tutorial rather than assuming exact CS50P lecture coverage.
  * Algorithmic decomposition, state machines, invariants, correctness proofs (loop invariants), complexity intuition (counting ops).
  * Python interpreter model, memory model (reference semantics), mutability vs immutability, scope (LEGB), closures, iterators vs generators vs async generators.
  * Branching, iteration, string manipulation, recursion (factorial, Fibonacci, Towers of Hanoi), debugging methodology, efficiency (big-O informal intro), tuples, lists, aliasing, cloning, mutating, dictionaries.
  * Optimisation problems, knapsack, graph-theoretic models, dynamic programming motivation, random walks, Monte Carlo simulation, sampling + confidence, experimental data curve-fitting, statistical myths.

* **Courses and references:**
  * **Primary Course Link:** [Harvard CS50P — free OpenCourseWare](https://cs50.harvard.edu/python/) · [MIT 6.0001 on OCW](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) · [University of Helsinki Python Programming MOOC](https://programming-26.mooc.fi/) (hands-on exercise-focused companion).
  * **Outcome-to-Resource Mapping:**
    * Core syntax & data structures (Lectures 0–2) → Variables, conditionals, loops, functions, lists, dicts.
    * Exceptions & file I/O (Lectures 3, 6) → Defensive parsing, `try/except`, `pathlib`, CSV/JSON handling.
    * Libraries & packaging (Lecture 4) → Standard library (`sys`, `random`, `json`), virtual environments.
    * Unit testing (Lecture 5) → `pytest`, automated test suites, fixtures, test-first assertions.
    * Object-oriented programming (Lecture 8) → Classes, methods, attributes, clean encapsulation.
    * Helsinki Python MOOC parts 1–7 → the same beginner-to-intermediate syntax, testing, file, and
      object-oriented outcomes through text-first, auto-tested practice; use it as a companion or depth
      alternative, not as an additional mandatory course.
  * **Access Status (Nov 2026):**
    * [CS50P](https://cs50.harvard.edu/python/) learning materials are free. Current official guidance
      says feedback/submission uses a free edX account, the CS50 Certificate route is free after
      completing requirements, and an edX verified certificate is optional and paid; the exact
      browser/GitHub workflow can change.
    * [Helsinki MOOC](https://programming-26.mooc.fi/) materials and exercise route are intended as a
      free companion with a MOOC.fi account; current certificate/ECTS terms are **not verified** here.
    * Local Python 3.12+, `uv`, `ruff`, and `pytest` are free open-source tools running offline.
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Fluent Python_ (**2nd Edition, 2022**; [fluentpython.com](https://www.fluentpython.com/) ✅) — Luciano Ramalho — chapters 1–6, 9 (closures/decorators), 17 (iterators).
    * _Python Crash Course_ (**3rd Edition**; [No Starch](https://nostarch.com/python-crash-course-3rd-edition) ✅) — Eric Matthes — for absolute beginners only.
  * **Practical Implementation:** Start in the browser (Scrimba, then [cs50.dev](https://cs50.dev/)). Professional tooling comes after CS50P; see below.

<details>
<summary><strong>Advanced / later (after CS50P):</strong> Python version, editor setup and Modern Python Tooling (uv, mypy, Pydantic, asyncio, hypothesis, pre-commit)</summary>

<a id="modern-python-tooling"></a>
* **Practical Implementation:** **Python 3.12+**, pinned to a version compatible with your dependencies. IDE: VS Code with Python and Ruff support. Dependency manager: **`uv`**, the roadmap's default; `venv` + `pip` is a valid alternative.


* **🛠 Modern Python Tooling:**
  * **Type hints + one type checker + Pydantic v2** — annotate your functions and validate untrusted data at API boundaries. `TypedDict`, `Protocol`, `Generic` and `Annotated` are later depth; see [Pydantic v2 docs](https://docs.pydantic.dev/).
  * **[`uv` project guide](https://docs.astral.sh/uv/guides/projects/)** — learn `uv init`, `uv add`, `uv run` and `uv lock`. Commit `pyproject.toml`, `.python-version` and `uv.lock`; reproduce with `uv sync --locked`.
  * **`async`/`asyncio`** — later depth for concurrent network I/O. Tokenization is usually CPU work; coroutines alone do not accelerate it. Read [Python asyncio](https://docs.python.org/3/library/asyncio.html) and optionally *Fluent Python* ch. 19–21.
  * **Git + GitHub Actions CI** — pre-commit hooks, branch-protection, conventional commits, GitHub Actions workflows for test/lint/build.
  * **`pytest`**, followed optionally by **`hypothesis`** — property tests are useful when you can state invariants. Learn `@given` and shrinking when a project needs them; see [Hypothesis docs](https://hypothesis.readthedocs.io/).
  * **`ruff` + `pyright`** for lint + typecheck; **`pre-commit`** to run them on every commit.

</details>

<a id="python-skill-groups"></a>
### 🎯 The four AI-engineering skill groups (v2026.7) + async (v2026.8)

You don't need all of Python to start building AI systems. Video W2 (01:15–02:28) narrows the foundation to **four skill groups**. v2026.8 adds a fifth, **[async concurrency and streaming](#async-skill-group)**, which you learn *after* the gate, right before Portfolio Spine L1. Application engineers often consume model APIs; training-oriented roles also need the later PyTorch modules. The [first 30 days](../guides/first-30-days.md#skill-groups) map each week onto these groups.

| # | Skill group | What it covers | Where you learn it | Free reference |
|---|---|---|---|---|
| **1** | **Core data & control flow** | Variables, lists, dicts, conditionals, `for`/`while`, functions, and *enough* OOP to read a class | Week 0 + CS50P Lectures 0–3 ([Weeks 1–4](../guides/first-30-days.md#week-1)), Lecture 8 later | [Python tutorial](https://docs.python.org/3/tutorial/) |
| **2** | **HTTP & JSON APIs + error handling** | Making requests, parsing JSON safely, API keys from environment variables (never in code), retries and timeouts | Week 4 `try`/`except` → [weather-CLI capstone](#m1-capstone) | [`requests`](https://requests.readthedocs.io/) · [`json`](https://docs.python.org/3/library/json.html) · [12-factor config](https://12factor.net/config) |
| **3** | **File & log I/O** | Reading documents, writing structured output, reading and writing logs | CS50P Lecture 6 → capstone cache | [`pathlib`](https://docs.python.org/3/library/pathlib.html) · [`logging`](https://docs.python.org/3/library/logging.html) |
| **4** | **Environment & package isolation** | One virtual environment per project with `venv` + `pip` or **`uv`**, so one project's library versions can't break another's | First local project (after cs50.dev) | [`venv` tutorial](https://docs.python.org/3/tutorial/venv.html) · [uv docs](https://docs.astral.sh/uv/) |

> **Group 4 is the one beginners skip** (W2, 02:13), and skipping it is what breaks your second project. The rule: **one project, one environment.** In cs50.dev the environment is managed for you. On your own machine, run `uv venv` or `python -m venv .venv` before your first `pip install`.

<a id="async-skill-group"></a>
### ⚡ Skill group 5 · Async concurrency, backpressure and token streaming (v2026.8)

> **When:** after the [3-check gate](#three-check-gate) and the [weather-CLI capstone](#m1-capstone), when your application needs concurrent I/O. This extension does not gate [Portfolio Spine L1](../guides/portfolio-spine.md#level-1) or M18-app. Groups 1–4 come first.

**Why it is a separate group.** Network calls can spend time waiting, and concurrency can overlap that wait. The gain depends on service latency, rate limits, connections and workload. Compare the same fixture at different concurrency limits; do not assume a throughput multiplier. See [HTTPX async](https://www.python-httpx.org/async/) and [Python task semantics](https://docs.python.org/3/library/asyncio-task.html).

| # | Competency | What "good" looks like | Free reference |
|---|---|---|---|
| **5a** | **`asyncio` + connection pooling** | One shared `httpx.AsyncClient` per process, opened with `async with` so connections are always closed, and explicit `httpx.Limits(max_connections=…)`. Never create a new client per request | [`asyncio`](https://docs.python.org/3/library/asyncio.html) · [HTTPX async](https://www.python-httpx.org/async/) · *Fluent Python* ch. 19–21 |
| **5b** | **Bounded concurrency** | Cap in-flight work with a semaphore; cap total retries/deadlines; a semaphore is not a rate limiter. Handle CPU-heavy work separately | [`asyncio.Semaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore) |
| **5c** | **Streaming (optional M24 extension)** | Measure TTFT and full latency, choose a workload-specific target, and close upstream streams on disconnect | [FastAPI streaming](https://fastapi.tiangolo.com/advanced/custom-response/) |
| **5d** | **Partial JSON + abort propagation** | Parse structured output *while it streams* (`partial-json-parser` turns `{"meal": "lentil so` into `{"meal": "lentil so"}`; [`instructor`](https://github.com/567-labs/instructor) offers `Partial[Model]` streaming). When the client disconnects, **stop the upstream generation**: a cancelled request that keeps generating still costs tokens | [`partial-json-parser`](https://github.com/promplate/partial-json-parser) · [`instructor`](https://github.com/567-labs/instructor) |

<a id="async-exercise"></a>
#### 🧪 Exercise: from a 100-call blocking loop to a rate-limited async pipeline

**Start (the blocking version you will replace):**

```python
import requests
results = [requests.post(API_URL, json={"prompt": p}, timeout=30).json()["text"]
           for p in prompts]          # 100 prompts × ~1.5 s each ≈ 150 s, and one exception kills the run
```

**Teaching sketch:** compare your implementation with the structure below. The endpoint and payload are placeholders, not a provider API contract. Run it only through the mock transport described below; it does not require a paid API. Test the claimed behavior in your own artifact rather than treating this sketch as an already-validated production client.

```python
import asyncio, os, httpx

API_URL = "https://fixture.test/read"           # custom mock fixture, not a provider API
MAX_IN_FLIGHT = 20                               # backpressure: never more than 20 open requests

async def call_llm(client, sem, prompt, retries=3):
    async with sem:                              # waits here while 20 calls are already in flight
        for attempt in range(retries):
            try:
                r = await client.post(API_URL, json={"prompt": prompt}, timeout=30.0)
            except httpx.TransportError:         # timeout / connection reset: retryable
                r = None
            if r is not None and r.status_code != 429 and r.status_code < 500:
                r.raise_for_status()             # other 4xx = our bug: fail fast, never retry
                return r.json()["text"]
            if attempt == retries - 1:
                raise RuntimeError(f"gave up after {retries} attempts: {prompt[:40]!r}")
            await asyncio.sleep(2 ** attempt)    # 1 s, 2 s backoff (honour Retry-After if sent)

async def run_all(prompts, transport=None):
    sem = asyncio.Semaphore(MAX_IN_FLIGHT)
    limits = httpx.Limits(max_connections=MAX_IN_FLIGHT, max_keepalive_connections=MAX_IN_FLIGHT)
    headers = {"Authorization": f"Bearer {os.environ.get('LLM_API_KEY', '')}"}
    async with httpx.AsyncClient(limits=limits, headers=headers, transport=transport) as client:
        results = await asyncio.gather(*(call_llm(client, sem, p) for p in prompts),
                                       return_exceptions=True)   # one failure never kills the batch
    print(f"{sum(not isinstance(r, Exception) for r in results)}/{len(prompts)} succeeded")
    return results

# Call run_all(..., transport=httpx.MockTransport(handler)) in your offline test.
# Supply an actual provider adapter only in the optional network extension.
```

**Test it without spending tokens.** The `transport=` parameter lets you pass `httpx.MockTransport(handler)`, where `handler` is an `async def` that sleeps 0.1 s, counts concurrent calls and returns a `429` the first time for one prompt and a `400` for another. Then assert: (1) peak in-flight never exceeds 20; (2) the `429` prompt succeeds on retry; (3) the `400` prompt is called exactly once; (4) the other 99 results are strings.

**Then add streaming (5c–5d).** The minimal SSE endpoint. Swap `fake_llm_tokens` for your provider's streaming iterator:

```python
import asyncio, json
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

async def fake_llm_tokens(prompt):               # stand-in for a provider's streaming API
    for tok in ["Lentil", " soup", " is", " high", " in", " protein", "."]:
        await asyncio.sleep(0.05)
        yield tok

@app.get("/chat")
async def chat(request: Request, q: str):
    async def event_stream():
        async for tok in fake_llm_tokens(q):
            if await request.is_disconnected():  # user closed the tab: stop paying for tokens
                break
            yield f"data: {json.dumps({'token': tok})}\n\n"     # one SSE event per token
        yield "event: done\ndata: {}\n\n"
    return StreamingResponse(event_stream(), media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})
```

**Done when:** (1) the async version handles 100 mock prompts with ≤ 20 in flight and isolated ordinary failures; (2) compare concurrency 1 and 20 on the same fixture and report measured runtime; (3) add timeout and cancellation cases and verify resources close; (4) record the cap and retry policy in [`DECISIONS.md`](../resources/templates/DECISIONS.md). A semaphore limits concurrency, not requests per second: real services may also need a rate limiter, a total deadline and bounded `Retry-After` handling. Retry side-effecting requests only with an explicit idempotency contract. Streaming is an optional M24 extension; measure TTFT for your workload rather than imposing a universal latency target.

> **Common mistakes:** creating a client inside a hot loop; scheduling an unbounded number of pending tasks (use a bounded queue for large streams); retrying invalid input; blocking the event loop. Default `gather` propagates the first exception **without automatically cancelling the other tasks**; `return_exceptions=True` collects ordinary errors. Preserve cancellation and close upstream streams explicitly. A partial JSON prefix is provisional: validate the complete response before acting on it.

<a id="ai-usage-rule"></a>
### 🚦 Foundations-phase AI usage rule and the 3-check exit gate

**The rule (W2, 05:08–05:26):** during Week 0, the first 30 days and M1 projects, **AI may only explain concepts and quiz you. You write the code yourself**, even when it's slow and frustrating. Letting an assistant write the project produces the *fluency illusion* (Video 1, 09:30): it feels like understanding, but you didn't do the work that makes it stick.

<a id="three-check-gate"></a>
**Exit gate: unlock AI coding assistants only when all three are true (W2, 05:27–05:41):**

| Check | How to test yourself (no AI, no hints) | ✅ |
|---|---|---|
| **1. Read** unfamiliar code | Open a 50–100-line Python file you didn't write (an Exercism community solution or a small open-source script). In 15 minutes, write one sentence per function saying what it does and what data goes in and out | ☐ |
| **2. Debug** a failing test alone | Break one assertion in your own `pytest` suite (or a [NumPy-sprint](../resources/numpy-from-scratch/README.md#numpy-from-scratch) test). Find and fix the cause from the traceback without pasting it into an LLM | ☐ |
| **3. Reason about data flow** | For your weather CLI, list in advance where it breaks on malformed input (bad city, timeout, a missing JSON key, an unwritable cache file). Then write one test per item | ☐ |

**After the gate, AI becomes a skill to practise, not a crutch to avoid** (W2, 05:50–07:15):

- **Spec-driven prompting.** Write the specification first, with constraints, inputs, outputs and failure cases. Then ask for an implementation. Ad-hoc one-line IDE prompts produce poor output.
- **Audit AI-written tests.** AI writes tests that pass for the wrong reasons. For every generated test, ask: *"Would this fail if the bug I care about came back?"*
- **Review generated code.** Check its behavior, assumptions and failure cases before committing it. AI-engineering roles also involve data, evaluation, systems and product work; their balance varies by team.
- **Write down the trade-offs.** Every project from here on records its choices in a [`DECISIONS.md`](../guides/portfolio-spine.md#decisions-template).

> The gate replaces the old "the policy loosens after M5" wording below for **coding assistants**. The M1–M5 policy still applies to maths and proof work.

### 📅 Suggested pacing structure — the four-phase Python roadmap

The topic list above is *what* to learn. The table gives illustrative pacing and a reviewable milestone for each phase. Adjust the weeks using your actual study time; the artifacts, not the dates, establish progress. Pacing and milestones are adapted from Scrimba's [beginner's guide to learning Python (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) and reconciled with the CS50P week map.

| Phase | Weeks | Goal | Core skills | **Milestone you must ship** |
| :--- | :--- | :--- | :--- | :--- |
| **1 — Foundations** | 1–4 | Stop being confused by syntax | Variables, types, operators, conditionals, loops, functions, lists/dicts/tuples/sets, string methods | A **number-guessing game** or a **command-line calculator** in a git repo with a README: the [M1 starter project](#m1-starter-project) |
| **2 — Working Python** | 5–8 | Write programs that touch the outside world | File I/O, CSV/JSON, exceptions, `pathlib`, modules + `import`, standard library, virtual envs, regular expressions | A **file-I/O CLI tool** (e.g. an expense tracker or file organiser) that reads and writes real files and survives bad input |
| **3 — Real-World Python** | 9–14 | Write code another engineer would accept | OOP (classes, inheritance, dunders), decorators, generators, comprehensions, type hints, `pytest`, `requests`, git branching + PRs, debugging | An **API-consuming application** with clear function boundaries, type hints and a `pytest` suite; CI is the stretch goal. This is the [M1 capstone](#m1-capstone) |
| **4 — Specialisation** | Month 4–6+ | Point Python at a domain | NumPy/pandas (→ [M7](2-statistics-and-data.md#module-7)), a web framework (Flask/FastAPI), Docker, deployment | **Later module artifacts with reproducible local demos** — see the [Minimum Production Bar](6-frontier-production.md#production-bar) |

**Phase-matched project ladder.** Match project difficulty to the phase you are actually in. Building above your rung produces copy-paste; building below it produces boredom.

| Rung | Phase | Project options |
| :--- | :--- | :--- |
| **Beginner** | 1 | Number-guessing game · password generator · Pomodoro timer · expense tracker · Markdown-to-HTML converter |
| **Intermediate** | 2–3 | Reddit scraper · Spotify listening-history analyser · Discord bot · weather CLI (real API + caching + error handling) · bulk file organiser |
| **Advanced** | 4 | Flask blog with authentication · sentiment analyser on a pretrained Hugging Face model · stock dashboard · RAG chatbot over your own notes |

> **Note on the advanced rung.** The sentiment analyser, stock dashboard and RAG chatbot can evolve into the [M16](5-deep-learning.md#module-16), [M14](4-probabilistic-ml.md#module-14) and [M21](6-frontier-production.md#module-21) projects respectively. Complete their prerequisites before claiming those modules. Reuse the relevant project instead of rebuilding it for a separate Python milestone.

<a id="python-course-matrix"></a>
### 🐍 Free Python course matrix

Choose one main course and add a companion only for a specific gap. This matrix is synthesised from Scrimba's [best free Python courses for beginners in 2026](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/), with historical checks in [`audit/VERIFICATION.md`](../audit/VERIFICATION.md). Access terms can change; use open CS50P materials as the default. Hour estimates describe different combinations of instruction and practice and are not directly comparable completion promises.

| Course | Hours | Format | Free certificate? | Projects | Best for |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[Scrimba — Learn Python](https://scrimba.com/learn-python-c03)** ✅ · **Week 0 default** | ~4.1 h · 3 sections | Interactive screencasts you can edit and run inline (Treasure Porth) | Yes (free certificate) | 3 projects: PayUp expense splitter, word-scramble game, karaoke queue manager | A browser-based start that avoids local environment setup. See [Week 0](../guides/week-0.md#week-0) |
| **[Harvard CS50P](https://cs50.harvard.edu/python/)** ✅ | ~100 h · 10 weeks | Lectures + graded problem sets (David Malan) | Yes (free certificate) | 9 problem sets + final project | The default lecture-based course; the spine of this module's topic list |
| **[University of Helsinki — Python Programming MOOC 2026](https://programming-26.mooc.fi/)** ✅ | 200+ h · 14 parts (two 5-ECTS courses: parts 1–7 and 8–14) | Text-based, auto-tested exercises; optional weekly lectures and recordings (Department of Computer Science, University of Helsinki) | Certificate/credit conditions vary; check course terms | Hundreds of auto-graded exercises | Learners who prefer **reading over watching** and want relentless exercise volume. **Depth alternative to CS50P** |
| **[freeCodeCamp — Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)** ✅ | ~300 h | Video + browser projects | Yes (free certification) | 5 certification projects | A **free credential** plus scientific-computing framing. ⚠️ Content is older than the others — verify Python-3 idioms against the official docs as you go |
| **[Official Python Tutorial](https://docs.python.org/3/tutorial/)** ✅ | ~15 h | Reference-grade prose | No | None | The **authoritative** source. Use as a companion, never as your first course |
| **[Google's Python Class](https://developers.google.com/edu/python)** ✅ | ~10 h | Written lessons + exercises | No | Small exercise sets | Programmers **already fluent in another language** who need Python syntax fast |
| **[Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)** ✅ | Book (3rd Ed., 2025) | Free full text online (Al Sweigart) | No | Chapter-end practice projects | Concrete examples of useful everyday automation |

<a id="python-helpers"></a>
**Free interactive helpers (use any time, never required):**

| Helper | What it does | Use it when |
| :--- | :--- | :--- |
| **[futurecoder](https://futurecoder.io/)** ✅ | Free interactive beginner course with hints, in the browser | A CS50P idea doesn't click and you want a second explanation |
| **[Python Tutor](https://pythontutor.com/)** ✅ | Visualises your code running, one line at a time | A loop or variable does something you didn't expect |
| **[Exercism — Python track](https://exercism.org/tracks/python)** ✅ | Free practice exercises with tests, an in-browser editor and optional volunteer mentoring | You want extra practice; the [first 30 days](../guides/first-30-days.md#week-3) uses five exercises |

> **The recommended pairing stack.** No single course produces competence. Run them in this order:
> **1. [Scrimba — Learn Python](https://scrimba.com/learn-python-c03)** for a frictionless [Week 0](../guides/week-0.md#week-0) →
> **2. [CS50P](https://cs50.harvard.edu/python/) *or* the [Helsinki MOOC](https://programming-26.mooc.fi/)** for the depth, testing discipline, and OOP that the fast courses skip. Pick CS50P if you learn from lectures; pick Helsinki if you learn from exercises. The [first 30 days](../guides/first-30-days.md#first-30-days) start CS50P for you →
> **3. Alongside, for motivation: [Automate the Boring Stuff](https://automatetheboringstuff.com/)** to turn syntax into things you actually use. Dip in when you want a fun side project; it is not a separate stage.
>
> Practise with the [free helpers](#python-helpers) above whenever you like.
>
> **Check a course's scope.** Use Python 3 for new work. A short introduction may omit OOP, exceptions or testing; add those topics before claiming the full M1 outcome. A course checklist alone does not establish employability.

### 🔨 How to actually study this module — the tutorial-hell escape protocol

Tutorial hell means repeatedly consuming instruction without practising independently. Use a small artifact to check whether you can apply what you watched.

1. **Start a small milestone.** Once you understand its first step, attempt it and turn the gaps into concrete, searchable questions.
2. **Close the tutorial and rebuild from memory.** Keep the original guided project and rebuild in a fresh file with the tab closed. What you cannot reproduce is what you have not learned — that list is your actual study plan.
3. **Protect practice time.** Try two hours of coding per hour of instruction as a planning experiment, then adjust using what you can explain and reproduce. No ratio diagnoses whether learning is happening.
4. **Read, break, and fix other people's code.** Clone a small open-source Python repo, read it until you can explain the entry point, deliberately break something, then fix it. Reading production code is a distinct skill from writing greenfield code, and job interviews test it.
5. **Keep a weekly learning log.** Share it privately or publicly if useful. Record what you built and the next question — see [Career Operations](../guides/career-operations.md#career-operations).

> **Check learning through performance:** explain a new example, reproduce a result and debug a failure. Feeling comfortable or struggling does not by itself establish understanding. Reduce scope or seek a different explanation when difficulty stops productive practice.

### 🤖 Disciplined AI-assistant practice

Use the three-check gate above for coding assistance. For M2–M5 mathematics and proofs, attempt the reasoning before requesting critique. The following examples apply before the coding gate and while practising an unfamiliar mathematical method.

**Useful requests during independent practice:**
* "Explain what this error message means and what category of bug causes it."
* "Review the code I already wrote and name the weaknesses — do not rewrite it."
* "Quiz me on decorators. Ask questions, do not give answers."
* "Explain three ways to structure this, with trade-offs" — then you choose and you type it.

**Avoid before you can independently explain and test the result:**
* "Write this function for me."
* Pasting a milestone project's requirements into a model and shipping the output.
* Accepting any autocomplete you could not have written yourself and cannot explain line by line.

> **⚠️ The fluency illusion.** Video 1 (09:30): *"There's this fluency illusion where AI hands you a perfect answer, and you walk away feeling like you understood it, but you didn't do the cognitive work that makes the knowledge stick."* Check your understanding by solving a fresh example and explaining a failure case without assistance.
>
> **Coding-assistant use follows the three-check gate above.** For M2–M5 proofs, attempt the derivation before requesting critique. Once you can explain and test the result, models can help with boilerplate, tests and configuration — and [M22](6-frontier-production.md#module-22) treats agentic coding as a first-class engineering topic. The restriction is developmental, not moral.

### 📚 Cited sources added in v2026.3

* **[Scrimba — *Best Free Python Courses for Beginners in 2026*](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/)** ✅ *(verified 2026-07-26)* — source for the [free Python course matrix](#python-course-matrix), the pairing stack, and the Python-2/no-OOP red flags.
* **[Scrimba — *How to Learn Python: A Beginner's Guide (2026)*](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/)** ✅ *(verified 2026-07-26)* — source for the four-phase pacing structure, the weekly milestones, the phase-matched project ladder, the tutorial-hell escape protocol, and the historical pacing discussion that preceded the current [role pathways](../guides/practitioner-track.md#practitioner-track).
* **Video 1 — [*How to Become an ML Engineer*](https://www.youtube.com/watch?v=UZ_rK9gzVSc)** (03:00–04:00) — the Python competence bar for ML work: data types, control flow, functions, and file handling, then straight into NumPy and pandas ([M7](2-statistics-and-data.md#module-7)). The *fluency illusion* warning is at 09:30.
* **Video 3 — [*The Only 7 Books You Need to Become an AI Engineer*](https://www.youtube.com/watch?v=Pr9oRVtAqCM)** (01:21) — Python is "table stakes" for the AI Engineer role; *Automate the Boring Stuff* is named as the entry point (see the [Practitioner Shelf](../resources/books.md#practitioner-shelf)).

<a id="m1-starter-project"></a>
* **🌱 M1 starter project (Weeks 3–4) — your first original program**
  * **When:** Week 4 of the [first 30 days](../guides/first-30-days.md#week-4), after CS50P Lectures 0–3.
  * **Deliverable:** pick **one** from the beginner rung of the [project ladder](#module-1). A **command-line calculator** that handles divide-by-zero and typos politely, *or* a **number-guessing game** with your own twist (limited guesses, a score or difficulty levels).
  * **Done when:** (1) it runs and survives one bad input; (2) it is in your `python-journey` repository; (3) its README records a normal run, a bad-input run and one lesson learned. Sharing is optional. Automated tests arrive at Lecture 5: this starter is a progress milestone, not full M1 completion.
  * *Why this exists:* a small, early win before the capstone. Dropout in programming MOOCs peaks in the first weeks ([Why this design](../guides/week-0.md#why-this-design)).

<a id="m1-capstone"></a>
* **📦 Module Project (mandatory, end-of-M1 capstone) — Weather CLI**
  * **When:** start around CS50P Lectures 5–6 (testing and files), after the starter project. It is a Phase 3 (Weeks 9–14) milestone.
  * **Deliverable:** A Weather CLI with city input, an API adapter, expiry-aware disk caching and readable output. Separate parsing, fetching, caching and formatting; use a class only when it clarifies state. Pin the Python/dependency environment. Bundle sanitized JSON fixtures and `--offline` mode so the artifact is reviewable without an account or network.
  * **Definition of done:** (1) mocked `pytest` tests for success, unknown city, timeout, malformed API data, cache expiry and an unwritable cache; (2) README with setup, usage and a fixture-output transcript; (3) useful errors and nonzero failure exit codes without credential leakage; (4) a short results memo with API provenance, limitations and diagnosed failures. When available, demonstrate the adapter against a free public weather service once; all automated assessment uses fixtures.
  * **Stretch (adds one production element):** Wire a GitHub Actions workflow that runs `ruff` + `pytest` on every push, and make the badge green.
  * *Archetype source: video 1 (13:40) — the "weather CLI with real API, caching and error handling" tier; Phase 3 milestone of the [four-phase roadmap](#module-1).*

---

<a id="module-2"></a>
## Module 2: Single-Variable & Multivariable Calculus + Matrix Calculus & Convex Optimisation

**Recommended principal reading:** Stewart, Clegg and Watson, **Calculus: Early Transcendentals**, ninth edition (Cengage, paid): differentiation/integration and multivariable practice. OpenStax Calculus is the free text alternative; the lectures stay free.

**Core outcome:** compute/check derivatives and integrals, use the multivariable chain rule and explain gradient descent. SVD derivatives, vector-field theorems, ODE adjoints and full convex duality are optional depth.

* **The Tutor's "Why":** Calculus explains local change and optimization. Learn derivatives and integrals first, then connect the chain rule to matrix calculus and automatic differentiation.

* **Strict Prerequisites:** High-school algebra and Module 1 (so you can verify integrals with SymPy). Module 0 proof literacy is recommended, not a gate. *Beginner note: Book of Proof ch. 1–4 is enough to start; the full Module 0 is optional.*

> **Sequencing note:** The matrix-calculus list below includes an advanced preview of derivatives through SVD and eigendecomposition. That preview is not a prerequisite for starting M2; the computational treatment of those decompositions belongs to M3, which can be taken before, after, or alongside M2.

* **Topic map (core plus optional depth; roadmap synthesis):**
  * Limits and continuity (ε-δ definition), derivative as a limit, power/product/quotient/chain rules, trig derivatives, exponential and log derivatives, implicit differentiation, linear/quadratic approximations, related rates, Mean Value Theorem, L'Hôpital's rule, optimisation (first/second derivative tests), Newton's method.
  * Antiderivatives, Fundamental Theorem of Calculus (both parts + proofs), u-substitution, integration by parts, trigonometric integrals, partial fractions, improper integrals, Riemann sums, numerical integration (trapezoidal, Simpson's rule), applications (areas, volumes of revolution, arc length, surface area, centre of mass, work).
  * Polar coordinates, parametric curves, conic sections, sequences, series convergence tests (ratio, root, integral, comparison, alternating series), power series, Taylor & Maclaurin series (**with remainder bounds — used in Newton's-method convergence and stochastic-gradient analysis**), complex numbers, Euler's formula.
  * Vectors in ℝⁿ, dot and cross products, lines and planes, vector-valued functions, partial derivatives, tangent planes, total differential, **gradient vector & directional derivatives** (the foundation of gradient descent), chain rule (multivariable), **Hessian matrix** (used in Newton's method and second-order optimisers), Lagrange multipliers (→ SVM dual), double/triple integrals, change of variables, Jacobian determinant, vector fields, line integrals, Green's theorem, Stokes' theorem, divergence theorem.
  * Function basics, domain/range, piecewise functions, composition, inverse functions; limits; differentiation applied to business problems; definite vs indefinite integration; matrix-vector product as linear combination (preview of M3).
  * Vector calculus for optimisation, constrained optimisation, Lagrange multipliers with KKT conditions, convex functions, Jensen's inequality, convex optimisation preview.
  * Calculus of variations (used in variational inference, M13).
  * **Differentials in the language of linear maps** (the *correct* modern view that subsumes both numerator-layout and denominator-layout conventions); derivatives of vector-valued functions of vectors (Jacobians); derivatives of scalar-valued functions of matrices (gradients); derivatives of matrix-valued functions of matrices (4-tensors / Kronecker products); chain rule as composition of linear maps; **forward-mode and reverse-mode automatic differentiation** (the operational foundation of every DL framework); cost analysis of forward-vs-reverse AD (matrix-multiplication-cost argument); derivatives through SVD, eigendecomposition, matrix inverse, determinant, log-determinant, trace, Frobenius norm; **adjoint method** for differentiating through ODE/PDE solutions (used in Neural ODEs and diffusion solvers, M16).
  * <details><summary><strong>Advanced / later:</strong> Stanford EE364A convex optimisation (Boyd) — topic list</summary>

    **Optional constrained-optimization topics:** Convex sets (hyperplanes, half-spaces, polyhedra, balls, ellipsoids, norm cones, positive semi-definite cone), operations preserving convexity, convex functions (definition via secant inequality, first- and second-order conditions, Jensen's inequality), epigraph, sub-level sets, conjugate function, **convex optimisation problems** (LP, QP, QCQP, SOCP, SDP and relevant ML formulations), Lagrangian duality, **KKT conditions**, strong vs weak duality, complementary slackness, perturbation analysis. Study the relevant Boyd–Vandenberghe sections when an SVM dual or constrained-optimization derivation requires this depth.

    </details>
  * **[The Matrix Cookbook — Petersen & Pedersen, 2024 update]** + **[Parr & Howard "The Matrix Calculus You Need For Deep Learning" (arXiv:1802.01528, 2024 revision)]** as *daily-reference* lookup PDFs.

* **Courses and references:**
  * **Primary Course Link:** [MIT OCW 18.01 Single Variable Calculus](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/) · [MIT OCW 18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/). Use the public videos, notes and exercises from these OCW routes.
  * **Matrix-Calculus track:** [MIT 18.S096 / 18.063 — Matrix Calculus for ML (IAP 2023 + Jan 2026)](https://github.com/mitmath/matrixcalc) — full lecture notes, video, problem sets *all open* on GitHub.
  * <details><summary><strong>Advanced / later:</strong> Convex-Optimisation track (Boyd)</summary>

    **Convex-Optimisation track:** [Stanford EE364A — Boyd, lectures + slides + book](https://web.stanford.edu/class/ee364a/) · [Free PDF of *Convex Optimization* (Boyd & Vandenberghe, Cambridge 2004, 6th printing 2023)](https://stanford.edu/~boyd/cvxbook/) · YouTube lecture series (re-recorded **Spring 2024**).

    </details>
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Calculus: Early Transcendentals_ (**9th Edition**) — James Stewart — chapters 1–12.
    * **[Recommended freely-available alternative]** _Active Calculus_ (Boelkins et al., **2024 edition, free online**) — an optional open-textbook route.
    * **[Free alternative]** Strang & Herman _Calculus, Vol 1–3_ (OpenStax, free PDF) — open textbook alternative.
    * _Mathematics for Machine Learning_ — Deisenroth, Faisal, Ong (**free author PDF**) — Chapters 5 (Vector Calculus), 6 (Probability), **7 (Continuous Optimization)**. [mml-book.com](https://mml-book.com/).
    * ***The Matrix Cookbook*** — Petersen & Pedersen (2024 web update) — [PDF mirror (University of Waterloo)](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf) (the former MIT 18.S096 mirror path now 404s; replaced v2026.7).
    * **Parr & Howard** "The Matrix Calculus You Need For Deep Learning" — free on arXiv `1802.01528` (revised); also as an HTML web-book at [explained.ai/matrix-calculus](https://explained.ai/matrix-calculus/).
    * <details><summary><strong>Advanced / later:</strong> Boyd & Vandenberghe reading</summary>

      **Boyd & Vandenberghe** _Convex Optimization_ (Cambridge 2004; **6th printing 2023**, free PDF as above) — chapters 1–5 for the optional convex-optimization branch; revisit later chapters as needed.

      </details>
    * 3Blue1Brown: [_Essence of Calculus_ playlist (16 videos, ≈ 3 hrs)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — required visual intuition.
  * **Practical Implementation:** **SymPy 1.13+** for symbolic verification; **JAX 0.7+** `jax.grad` / `jax.jacrev` / `jax.jacfwd` / `jax.hessian` for automatic differentiation — learn these NOW as you'll need them for all of M15+. **`cvxpy` 1.5+** for convex optimisation modelling (DCP), **`autograd`** as a teaching aid for hand-coding back-prop. Optionally explore **`Zygote.jl`** in Julia for source-to-source AD intuition.

* **🌱 Beginners:** your college calculus course plus 3Blue1Brown's *Essence of Calculus* is enough to start the [module project](#module-2). The 16-week plan below is a later, full-depth option, not a prerequisite for anything in your first year.

* **Suggested Sequencing (full depth, later — 16 weeks at 10 hrs/week):**
  1. Weeks 1–4: Single-variable calculus using the selected MIT OCW 18.01 materials.
  2. Weeks 5–6: Series and Taylor approximations using the corresponding OCW 18.01 topics.
  3. Weeks 7–10: Multivariable (18.02 SC), with daily SymPy verification.
  4. Optional later depth: **Matrix calculus** (MIT 18.063 + Parr-Howard), after the linear-algebra concepts used by the selected derivation.
  5. Optional later depth: **Convex optimisation** (EE364A) — formulate selected `cvxpy` examples (LP, LASSO, SVM, portfolio or logistic regression).

* **🧠 Automatic Differentiation Theory (2026.2 NEW sub-section):** Understanding AutoDiff is non-negotiable for M15+.
  * **Forward-mode (JVP — Jacobian-Vector Product):** Propagate tangents through the computation. One JVP has work comparable to a function evaluation; a full Jacobian needs one direction per input. Often preferable when **inputs ≪ outputs**.
  * **Reverse-mode (VJP — Vector-Jacobian Product):** Propagate cotangents backward. One VJP has work comparable to a function evaluation plus intermediate storage/recomputation; a full Jacobian needs one seed per output. This makes backpropagation useful for a scalar loss with many parameters.
  * **Mixed-mode:** For Hessian-vector products (`Hv = ∇(∇L · v)`) used in second-order optimisers, Newton-CG, and natural gradient — apply forward-over-reverse or reverse-over-forward.
  * **Checkpointing:** Trade compute for memory by recomputing activations during backward pass (used in FSDP / gradient-checkpointing in M15).
  * **Practical:** `jax.grad`, `jax.jvp`, `jax.vjp`, `jax.jacrev`, `jax.jacfwd`, `jax.hessian`; `torch.autograd.grad`, `torch.func.vmap`, `torch.func.jacrev`; all cross-reference the [MIT 18.063 matrix-calc notes](https://github.com/mitmath/matrixcalc) already cited above.

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The introductory route:** watch [3Blue1Brown — *Essence of Calculus*](https://www.3blue1brown.com/topics/calculus) for derivative-as-rate-of-change and chain-rule pictures, then [StatQuest's gradient-descent series](https://statquest.org/). *The Manga Guide to Calculus* is an intuition companion. Attempt the finite-difference example below and explain what automatic differentiation computes. This introduction does not replace full M2's mathematical outcomes and gradient-descent project.
>
> **The argument for it:** Video 1 (01:41–02:06) puts 3Blue1Brown and StatQuest at Phase 1 and budgets **2–4 weeks** for "a rough mental map rather than mastery." Video 3's speaker reports never hand-computing a chain rule in six years at Amazon and Coursera (04:47).
>
> **What you give up — stated plainly:** The short route covers gradient intuition and computational checks, but not full convergence proofs or constrained duality. Study the relevant derivation when your model or research question requires it.
>
> **Complete the relevant core before:** continuous probability in [M5](#module-5), regression in [M9](3-classical-ml.md#module-9) and backpropagation in [M15](5-deep-learning.md#module-15). Return to EE364A when a selected derivation requires convex duality or constrained optimization.

* **📦 Module Project (mandatory) — Gradient-descent laboratory**
  * **Deliverable:** A small NumPy package that minimises a user-supplied scalar function. Implement (a) finite-difference gradients, (b) analytic gradients for three test functions (quadratic bowl, Rosenbrock, logistic loss), and (c) plain gradient descent, momentum, and Adam. Plot the optimisation trajectory over a contour map for each.
  * **Definition of done:** (1) `pytest` suite asserting that your analytic gradient matches the finite-difference gradient to a documented tolerance appropriate to the dtype, scale, and step size (use `1e-6` for the stated float64 fixtures); (2) `README.md` with the three contour plots and a table of iterations-to-convergence per optimiser; (3) a results memo comparing the optimisers on the same learning-rate/search budget rather than assuming momentum always wins on Rosenbrock.
  * **Stretch:** Reproduce your Adam result using `jax.grad` and show the two agree — this is your bridge into [M15](5-deep-learning.md#module-15).
  * *Application subset: implement finite differences and plain gradient descent, then compare with the analytic derivative of a quadratic. Momentum, Adam and derivations are full-module depth.*

---

<a id="module-3"></a>
## Module 3: Linear Algebra — Computational, Geometric & Abstract

**Recommended principal reading:** Gilbert Strang, **Introduction to Linear Algebra**, sixth edition (Wellesley-Cambridge Press, paid): systems, subspaces, projections, eigenvalues and SVD. Match exercises to your edition rather than copying older OCW page numbers.

**Core outcome:** solve linear systems, explain rank/projection, compute SVD/PCA and diagnose ill-conditioning. The three core experiments below establish application fluency; Axler proofs and sparse iterative solvers are optional depth.

* **The Tutor's "Why":** Vectors, projections and factorizations connect regression, dimensionality reduction and neural networks. Strang provides the computational route; [Axler's open fourth edition](https://linear.axler.net/) is a proof-oriented second pass. Completing both books is not required before applying linear algebra.

* **Strict Prerequisites:** High-school algebra for the mathematics; M1 Python skills before the computational project.
* **Recommended Prerequisites:** Module 0b (proof literacy; *Book of Proof* ch. 1–4). Module 2 (calculus) is recommended concurrently or needed later when connecting matrix calculus to optimization ([Module 9](../curriculum/3-classical-ml.md#module-9) and [Module 15](../curriculum/5-deep-learning.md#module-15)), but is not a blocker for linear algebra fundamentals (vector spaces, linear independence, projections, and eigenvalues).
* **Prior Competency:** Demonstrated high-school algebra or prior computational maths waives prerequisites.

* **🧭 Suggested Two-Pass Pedagogy:**
  * **Pass 1 — Computational (5 weeks):** Strang 18.06 + 3Blue1Brown — focus on *doing* row-reduction, computing eigenvalues, running SVD on toy matrices. Goal: numerical fluency.
  * <details><summary><strong>Advanced / later:</strong> Pass 2 — Abstract (Axler)</summary>

    **Pass 2 — Abstract (4 weeks):** Axler 4e (Chapters 1–7, skipping Chapter 8 if PhD-track is not the goal) — focus on *proving* spectral theorem, why SVD always exists, why orthogonal projection minimises distance. Goal: theoretical confidence.

    </details>
  * **Pass 3 — Applications (3 weeks):** Strang's *Linear Algebra and Learning from Data* + Fessler and Nadakuditi's *Linear Algebra for Data Science, Machine Learning, and Signal Processing* (Cambridge 2024) — focus on *the eight matrix factorisations of ML* (LU, QR, eigendecomposition, SVD, Cholesky, polar, NMF, randomised SVD).

* **Topic map (core plus optional depth; roadmap synthesis):**
  * Systems of linear equations, Gaussian elimination, LU factorisation, vector spaces, subspaces (column space, null space, row space, left null space — the "four fundamental subspaces"), rank-nullity theorem, linear independence, basis, dimension, orthogonality, Gram-Schmidt process, QR decomposition, projections, least squares (normal equations), determinants (cofactor expansion, properties), **eigenvalues and eigenvectors** (characteristic polynomial, diagonalisation), **Singular Value Decomposition (SVD)** (full and reduced forms, Eckart-Young theorem, pseudoinverse), positive-definite matrices (Cholesky), similar matrices, Jordan form, complex matrices (Hermitian, unitary), fast Fourier transform as a change of basis, linear transformations, applications to graphs (Laplacian), applications to differential equations (matrix exponential).
  * <details><summary><strong>Advanced / later:</strong> Axler abstract-pass topic list</summary>

    **[Axler — *Linear Algebra Done Right* 4e (2024) · *abstract pass*]**: Vector spaces *axiomatically* (no a-priori reference to ℝⁿ), subspaces, sums and direct sums, linear independence, basis, dimension; **linear maps as the central object** (kernel, image, the fundamental theorem of linear algebra); polynomials over ℂ (the algebraic backbone of eigentheory); eigenvalues, eigenvectors, **invariant subspaces, generalised eigenspaces**; **inner-product spaces** (axioms, Cauchy-Schwarz, triangle inequality, orthonormal bases via Gram-Schmidt, orthogonal complements, orthogonal projection as best approximation); **operators on inner-product spaces** (self-adjoint, normal, **the Spectral Theorem — proven without determinants**, polar decomposition, **SVD via the spectral theorem**); positive operators and isometries; trace and determinant *properly* defined (via characteristic polynomial coefficients, not as the Leibniz formula).

    </details>
  * **[3Blue1Brown — Essence of Linear Algebra (16 videos, evergreen)]**: Geometric intuition for determinants as signed-volume scaling, eigenvectors as invariant directions, change of basis as relabelling, **dot product as the dual of a linear map** (the trick that makes attention "queries · keys" feel inevitable).
  * Matrix rank via row reduction, solvability of linear systems, null space / column space correspondence, linear maps, basis transformations, symmetric matrices and spectral theorem.
  * Inner product spaces, orthogonal complement, projection matrices `P = A(AᵀA)⁻¹Aᵀ`, quadratic forms, positive semi-definiteness as condition for convex loss.
  * Vector spaces as abstract objects, bases, inner products, orthonormal bases, projection onto subspace, **"model fitting as projection"** (critical insight for understanding linear regression), design of features, basis functions (polynomial, Fourier, radial).
  * Eigendecomposition as diagonalisation, SVD applications to dimensionality reduction and image compression.
  * Condition number κ(A) and numerical-stability intuition, **why floating-point matters** (catastrophic cancellation; why you never `(AᵀA)⁻¹Aᵀy` in practice — use `np.linalg.lstsq` or QR), **randomised SVD** (Halko-Martinsson-Tropp, 2011 — a method for low-rank approximation), iterative methods (power iteration, Lanczos, Arnoldi → ARPACK), **Krylov subspaces** as preview of conjugate-gradient.

* **Courses and references:**
  * **Primary Course Link:** [MIT 18.06 OCW SC version (Strang, 2011) — evergreen](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) · [3Blue1Brown EoLA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  * <details><summary><strong>Advanced / later:</strong> Abstract / Proof Track (Axler)</summary>

    **Abstract / Proof Track:** [_Linear Algebra Done Right_ — Axler, **4th Edition, Springer 2024, FREE PDF + Kindle**](https://linear.axler.net/) — a proof-oriented second course; 400 pp.; includes worked solutions.

    </details>
  * **Optional paid applications text:** [_Linear Algebra for Data Science, Machine Learning, and Signal Processing_ — Jeffrey A. Fessler and Raj Rao Nadakuditi (Cambridge, 2024)](https://www.cambridge.org/highereducation/books/linear-algebra-for-data-science-machine-learning-and-signal-processing/1D558680AF26ED577DBD9C4B5F1D0FED). The publisher confirms the authors and edition.
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Introduction to Linear Algebra_ (**6th Edition, 2023**) — Gilbert Strang. Companion to 18.06.
    * _Linear Algebra and Learning from Data_ (**2019**) — Strang — specifically written for ML era; covers randomised SVD, NMF, neural-net Jacobians.
    * <details><summary><strong>Advanced / later:</strong> Axler reading</summary>

      ***Linear Algebra Done Right* (Axler, 4e, 2024)** — selected chapters 1–7 for the optional abstract pass.

      </details>
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapters 2, 3, 4.
    * **[*Numerical Linear Algebra* — Trefethen & Bau (SIAM, 1997, 25th-anniversary printing 2022)]** — for any student going into systems / scaling ([M24](6-frontier-production.md#module-24)).
  * **Free interactive notebooks:** [`fastai/numerical-linear-algebra` — Rachel Thomas USF (2019, open teaching notebooks, all-Jupyter)](https://github.com/fastai/numerical-linear-algebra) — covers SVD, randomised methods, PageRank, compressed sensing in 12 lectures.
  * **Practical Implementation:** **NumPy 2.x** (`np.linalg.eig`, `np.linalg.svd`, `np.linalg.solve`, `np.linalg.lstsq`). **SciPy 1.14+** for sparse linear algebra (`scipy.sparse.linalg`, ARPACK eigensolvers, `splu`). Use **`jax.numpy`** for GPU-accelerated linear algebra once comfortable. **`einops` 0.8+** to write tensor operations in *index notation* — useful for tracking tensor shapes in later attention implementations.

* **Mini-project menu: complete 1, 2 and 4 for the core; 3 and 5 are optional graph applications.**
  1. **PCA on MNIST from scratch** using only `np.linalg.svd` — recover 95 % variance in `k` components, plot `k`.
  2. **Image compression** via truncated SVD on a single greyscale photo — show MSE-vs-rank curve.
  3. **PageRank** as power iteration on the link-matrix — verify on a 5-node toy graph by hand.
  4. **Linear regression by four methods** — explicit normal-equation inverse *vs* `np.linalg.lstsq` *vs* QR *vs* SVD; compare residual and parameter errors on Hilbert matrices, measuring condition number for each size and dtype.
  5. **Spectral clustering** on the two-moons dataset — Laplacian eigenmaps in 30 lines.

  **Shared definition of done:** Put the selected experiments in one reproducible package. Add tests for
  matrix shapes, reconstruction and explained-variance invariants; test the hand-checkable PageRank
  graph only if choosing that extension. Include a clear `README.md` with plots and numerical tolerances, plus a
  short results memo explaining one stability failure or misleading result. Use local fixtures or a
  small downloaded subset so the project is CPU-runnable.

* **🔢 Numerical Linear Algebra (2026.2 NEW sub-section):** Production ML code that gets this wrong silently corrupts training.
  * **Factorisations used in ML:** LU (solving Ax=b), Cholesky (SPD systems, Gaussian MLE, KFAC), QR (least-squares, Gram-Schmidt, Arnoldi), **Householder reflections** (numerically stable QR — the *right* way), SVD (low-rank approx, pseudoinverse, PCA), **randomised SVD** (Halko-Martinsson-Tropp — standard for embedding compression at scale).
  * **Iterative solvers:** Conjugate Gradient (CG) for large sparse SPD systems, Lanczos/Arnoldi for dominant eigenvalues, GMRES for non-symmetric. These matter for Gaussian-Process inversion (M13), natural gradient (M17), and implicit differentiation through optimisation (M15).
  * **Condition number & stability:** Compare `np.linalg.lstsq(A, b)` with explicit inversion of the normal equations; report actual errors and conditioning instead of assuming a fixed accuracy multiplier. Read *Trefethen & Bau* Lectures 12–16 for optional depth.
  * **Floating-point traps:** catastrophic cancellation, log-sum-exp trick, Kahan summation, mixed-precision (bf16/fp16/fp8) for DL.

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The introductory route:** watch [3Blue1Brown — *Essence of Linear Algebra*](https://www.3blue1brown.com/topics/linear-algebra), optionally with *The Manga Guide to Linear Algebra*, then try the PCA mini-project. This builds geometric intuition and is a useful starting milestone. Full M3 still requires its core outcomes and mini-projects 1, 2 and 4; a video playlist alone does not supply that competence.
>
> **The argument for it:** Video 1 (01:41–02:06) names Essence of Linear Algebra specifically as the Phase 1 resource, with the goal being a mental map, not mastery.
>
> **What you give up — stated plainly:** The shortened route gives less practice with proofs and numerical methods. Keep the PCA reconstruction check and a conditioning example; revisit projections/SVD when you cannot justify a preprocessing choice.
>
> **Complete the core before:** [M9](3-classical-ml.md#module-9), [M11](3-classical-ml.md#module-11), [M13](4-probabilistic-ml.md#module-13) and [M15](5-deep-learning.md#module-15). Revisit numerical linear algebra when conditioning or approximation errors affect a result.

---

<a id="module-4"></a>
## Module 4: Discrete Math, Algorithms & Data Structures

**Recommended principal reading:** Cormen, Leiserson, Rivest and Stein, **Introduction to Algorithms**, fourth edition (MIT Press, paid): asymptotics, data structures, graph algorithms and dynamic programming. Use selected chapters with free MIT 6.006 lectures, not a cover-to-cover gate.

**Core outcome:** choose lists/maps/heaps, analyze time and space, implement traversal and a small dynamic program, and formulate/test the meal planner. Streaming sketches and approximation theory are optional depth. Use MIT 6.006 as the free default; the other courses and books are alternatives.

* **The Tutor's "Why":** Interviews for FAANG/quant/research roles test DSA rigorously; beyond that, you cannot design feature pipelines (hashing, bloom filters) or understand graph ML without it. **Cambridge ML & Bayesian Inference (2025-26) explicitly lists Discrete Mathematics as a prerequisite.**

* **Strict Prerequisites:** Module 1 (can write and debug Python).
* **Recommended Prerequisites:** Module 0b proof literacy and Module 5 probability for the randomized
  and streaming extensions. Neither is a blocker for the core data-structures and algorithms path.

* **Topic map (core plus optional depth; roadmap synthesis):**
  * ArrayList implementation, singly/doubly linked lists, stacks, queues, circular buffers, amortised analysis of dynamic arrays.
  * Binary trees, BST operations (insert, delete, search, traversal — in/pre/post-order, level-order), heaps (min-heap, max-heap, heapsort, priority queue), skip lists, hashmaps (open addressing vs chaining, load factor, rehashing, perfect hashing).
  * Self-balancing trees — AVL (rotations, balance factor), 2-4 trees, red-black trees, B-trees (used in databases — Module 8), divide-and-conquer (master theorem, merge sort, quicksort, strassen matrix multiplication).
  * Pattern matching (Boyer-Moore, KMP, Rabin-Karp), graph algorithms (BFS, DFS, topological sort), **Dijkstra's shortest path**, Bellman-Ford, **Minimum Spanning Tree (Prim's, Kruskal's)**, dynamic programming (LCS, edit distance, knapsack, matrix-chain multiplication), NP-completeness, approximation algorithms.
  * Complexity analysis (O, Ω, Θ), master theorem proofs, graph representations (adjacency list/matrix), topological sort with DFS, DAG shortest paths, strongly connected components (Tarjan, Kosaraju).
  * Proof techniques (induction, contradiction, contrapositive), set theory, relations, equivalence classes, partial orders, functions (injection, surjection, bijection), counting (permutations, combinations, inclusion-exclusion, pigeonhole), recurrence relations, generating functions (preview of MGFs in M5), graph theory (Euler paths, Hamiltonian cycles, planarity, chromatic number), elementary number theory (gcd, Euclidean algorithm, modular arithmetic — used in cryptography and hashing).
  * **Social networks analysis** — properties of networks (degree, diameter), betweenness centrality, clustering using betweenness centrality, detection of cliques in unstructured networks.
  * **[2026.2 addendum — Randomised & Streaming Algorithms]**: **Bloom filters** (false-positive rate calculus, counting bloom, cuckoo filter), **MinHash / locality-sensitive hashing (LSH)** (Jaccard similarity estimation for dedup and near-duplicate detection, used in LLM pre-training data pipelines), **HyperLogLog** (cardinality estimation), **Count-Min Sketch** (frequency estimation for streaming), **reservoir sampling** (uniform sampling from a stream of unknown length), **randomised quicksort**, **Karger's min-cut**. *Choose these extensions for data-system workloads where their trade-offs matter.*
  * **[Amortised Analysis]**: Aggregate / accounting / potential methods applied to dynamic arrays, splay trees, union-find with path-compression — the mental model behind *"why Python `list.append` is O(1) amortised"*.
  * **[Approximation Algorithms]**: PTAS / FPTAS definitions, vertex-cover 2-approximation, set-cover greedy log-factor, k-means approximation, **primal-dual schema** — relevant for NP-hard pipeline-scheduling problems (M8b).

* **Courses and references:**
  * **Primary Course Link:** [MIT 6.006 Introduction to Algorithms OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — free lectures, notes and Python exercises.
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Introduction to Algorithms_ (**4th Edition, 2022**) — Cormen, Leiserson, Rivest, Stein (CLRS) — the canonical reference.
    * _Algorithm Design Manual_ (**3rd Edition, 2020**) — Skiena — for problem-solving intuition.
    * _Concrete Mathematics_ (**2nd Edition**) — Graham, Knuth, Patashnik — for discrete-math depth.
  * **Practical Implementation:** Pure Python + `collections` (deque, defaultdict, Counter), **`sortedcontainers`**, **`networkx` 3.x** for graph algorithms, **LeetCode** + **Codeforces** for practice.

* **📦 Module Project (mandatory) — Constraint-based meal planner**
  * **Deliverable:** A program that, given a food database (calories + macros + cost per item) and a set of constraints (daily calorie target, minimum protein, budget ceiling, no more than *k* repeats per week), produces a valid 7-day meal plan. Solve it twice: once with your own search/DP formulation, once with a solver (`pulp` or `ortools`), and compare.
  * **Definition of done:** (1) `pytest` suite including at least one *infeasible* constraint set that your program correctly reports as unsatisfiable rather than crashing or silently returning garbage; (2) `README.md` stating the formulation explicitly — decision variables, objective, constraints; (3) a results memo comparing your hand-rolled search against the solver on runtime and solution quality, and stating the complexity class of the problem you just solved.
  * **Stretch:** Expose it as a Streamlit app so a non-programmer can change the constraints and see a new plan.
  * *Archetype source: video 1 (14:05) — the constraint-based meal planner, cited there specifically because it demonstrates problem formulation rather than model-fitting.*

---

<a id="module-5"></a>
## Module 5: Probability Theory — The Language of Uncertainty

**Recommended principal reading:** Blitzstein and Hwang, **Introduction to Probability**, second edition (author-provided free text; paid print): conditional probability, random variables, expectation and limits.

**Core outcome:** conditional probability, expectation/variance, common distributions, LLN/CLT and Monte Carlo error. Complete the simulation project; measure theory and advanced concentration are optional research depth.

* **The Tutor's "Why":** Probability describes sampling and uncertainty. Conditional distributions connect prediction with evidence; simulations make the assumptions and variability visible before inference in M6.

* **Strict Prerequisites:** Module 1 for simulations and the single-variable calculus core of Module 2 for continuous distributions.
* **Recommended Prerequisites:** Module 3 before covariance matrices and multivariate Gaussian extensions. Discrete probability can begin while calculus is in progress.

* **Topic map (core plus optional depth; roadmap synthesis):** Stat 110 is the main course. Match topics to its actual lecture titles; the roadmap's additional topics and sequence are not a transcript of one offering.
  * Probability and Counting — sample spaces, events, naïve definition of probability, multiplication rule, permutations, combinations, binomial coefficient identities.
  * Story proofs, axioms of probability (Kolmogorov), inclusion-exclusion.
  * Birthday problem, properties of probability (monotonicity, Bonferroni).
  * Conditional probability, Law of Total Probability, Bayes' Theorem, **Monty Hall**, **Simpson's Paradox**.
  * Gambler's ruin, random variables, CDF, PMF.
  * **Expectation** — linearity of expectation (with non-independent RVs!), indicator RVs, fundamental bridge.
  * **Poisson distribution** — Poisson paradigm, Poisson approximation to binomial.
  * Discrete vs continuous RVs, **Uniform**, **Normal** (standard and general), 68-95-99.7 rule, universality of the uniform.
  * Location, scale, **LOTUS** (Law of the Unconscious Statistician).
  * **Exponential distribution** — memorylessness, connection to Poisson process.
  * **Moment Generating Functions (MGFs)** — uniqueness, computing moments, MGF of sums of independent RVs.
  * **Joint, conditional, and marginal distributions**, independence, transformations.
  * **Multinomial**, Cauchy (and why its mean doesn't exist).
  * **Covariance and Correlation**, Cauchy-Schwarz.
  * Transformations of random variables, **convolutions** (sum of RVs).
  * **Beta distribution** — conjugate prior for binomial (preview of M13).
  * **Gamma distribution**, Poisson process in detail, arrival times.
  * **Order statistics**, **conditional expectation** as an RV, Adam's law (E[E[Y|X]] = E[Y]), Eve's law (law of total variance).
  * **Inequalities** — Markov, Chebyshev, Cauchy-Schwarz, Jensen, Chernoff bounds.
  * **Law of Large Numbers** (weak and strong), **Central Limit Theorem** (statement and MGF proof).
  * **Chi-squared**, **Student-t**, **Multivariate Normal** (mean vector, covariance matrix, conditional MVN).
  * **Markov chains** — transition matrix, stationary distribution, reversibility, convergence (detailed balance preview for MCMC).
  * A look ahead — Brownian motion, martingales.
  * Complements Stat 110 with a more engineering-flavoured treatment — probability spaces, conditioning as information update, Bayesian vs frequentist views introduced, discrete/continuous RVs, multiple RVs, derived distributions, convergence in probability vs distribution vs almost sure, Bernoulli process, Poisson process, elementary queueing, hidden random processes.
  * Types of data and scales of measurement (nominal/ordinal/interval/ratio), descriptive vs inferential statistics; frequency distributions; measures of central tendency (mean/median/mode) with formal definitions; measures of dispersion (range, variance, standard deviation, IQR); five-number summary and boxplots; association (contingency tables, Pearson correlation, point-biserial correlation); counting principles (addition/multiplication rule, factorials); permutations and combinations; probability (events, axioms); conditional probability, multiplication rule, independence, law of total probability, Bayes' theorem; random variables (PMF, CDF); expectation and variance of discrete RVs; Bernoulli trials, binomial, Poisson; continuous RVs (uniform, exponential).
  * PDF and CDF manipulation, Bayes's rule, **Monte Carlo estimation** (first rigorous introduction), empirical distribution as a function.
  * Markov chains (discrete time), **stationarity and drift analysis**, processes with memory, learning a random process from data.

* **Extended topic menu:** concentration inequalities and measure theory below are optional research depth. Entropy, conditional expectation and Monte Carlo estimation are the application core.
  * **Concentration inequalities for ML — beyond Chebyshev:** **Hoeffding's inequality** (the workhorse of generalisation bounds), **McDiarmid's bounded-differences inequality**, **Bernstein's inequality**, **sub-Gaussian** and **sub-exponential** random variables, ψ-Orlicz norms, **Bernstein-Chernoff bound for VC-dimension** (the 1971 Vapnik-Chervonenkis result that started statistical learning theory). Study the inequalities needed by the particular generalization bound you choose.
  * **Information theory primer (the overlap with probability):** **entropy `H(X) = −Σ p log p`**, joint and conditional entropy, **mutual information `I(X;Y)`**, **KL divergence `D_KL(P‖Q)` and Jensen's inequality**, cross-entropy (a common classification and language-modeling objective), **f-divergences** (TV, JS, Hellinger), **Fano's inequality** (lower bounds for classification error). Use the matching sections in Cover and Thomas; the advanced inequalities are optional.
  * **Measure-theoretic bridge — *taught minimally so you can read PML2 (Murphy 2023)*:** σ-algebras (Borel), measurable functions, Lebesgue integral *vs* Riemann (why we need it: integrating discontinuous limits), **Radon-Nikodym derivative `dν/dμ`** (the *correct* definition of "density"), almost-sure convergence vs convergence in probability vs in distribution vs in `L²`, pushforward measures, **dominated and monotone convergence theorems** (conditions that can justify exchanging limits and integrals). **Goal:** read Wasserman *All of Statistics* Ch 21 or Murphy PML2 Ch 1 without panic — *not* to do measure-theoretic exercises.
  * **Probability in code — *do these three concretely*:** (1) **inverse-CDF sampling** for a distribution with a tractable quantile function, hand-coded; (2) **rejection sampling** + **importance sampling** with diagnostics (effective sample size); (3) **Monte-Carlo integration** of a 5-D integral with confidence-interval analysis.

* **Courses and references:**
  * **Primary Course Link:** [Harvard Stat 110 lecture playlist](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) and [author course materials](https://stat110.hsites.harvard.edu/) — free lectures, text and practice materials.
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Introduction to Probability_ (**2nd Edition, 2019**) — Joseph Blitzstein & Jessica Hwang — [author-provided text and course resources](https://stat110.hsites.harvard.edu/). Select conditional probability, random variables, expectation/variance, continuous distributions and limit-theorem chapters for the core; later stochastic-process topics are depth.
    * _Introduction to Probability_ (**2nd Edition, 2008**) — Bertsekas & Tsitsiklis — companion to 6.431x.
    * **[_Introduction to Probability for Data Science_ — Stanley H. Chan (Michigan Publishing; free author-hosted text)](https://probability4datascience.com/)** — a computational companion with Python/MATLAB examples.
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapter 6.
    * **[_Information Theory, Inference, and Learning Algorithms_ — David MacKay (Cambridge 2003, **free PDF**)](https://www.inference.org.uk/itila/)** — chapters 1–6 provide an information-theory companion with exercises.
    * **[_High-Dimensional Probability_ — Roman Vershynin (Cambridge 2018, **free draft online**)](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html)** — *the* reference for sub-Gaussian, concentration, and random matrices; chapters 1–3 sufficient for ML purposes.
    * **(Optional, PhD-track only)** _Probability with Martingales_ — David Williams (Cambridge 1991), or _Measure, Integral and Probability_ — Capinski & Kopp (Springer 2nd ed., 2014) — for the measure-theoretic complement after Stat 110.
  * **Practical Implementation:** NumPy `np.random.default_rng(seed)` and SciPy `stats` for CPU simulations. Differentiable-distribution libraries belong to later Bayesian/DL work; they are not needed for M5.

* **Suggested sequence (adjust to your available study time):**
  * Begin with counting, conditional probability, random variables and expectation; solve selected problems and build the birthday/Monty Hall simulations below.
  * Add variance, continuous distributions, sampling, LLN and CLT; compare analytic quantities with simulation uncertainty.
  * Complete the shared simulation project and explain the limits of its conclusions. Entropy and conditional expectation prepare later ML reading.
  * Concentration inequalities, advanced stochastic processes and measure theory are optional research depth after the core.

> ### ⚡ Intuition-First Alternative (Practitioner Track)
>
> **The introductory route:** use [StatQuest's probability and statistics playlists](https://statquest.org/) and *The Manga Guide to Statistics* for intuition, then attempt a conditional-probability example and CLT simulation. This is preparation; full M5 completion still requires its core outcomes and simulation project.
>
> **The argument for it:** Video 1 (02:18–02:42) treats probability as something absorbed through StatQuest alongside ML overviews rather than as a standalone 12-week course. Video 3 (06:03) makes StatQuest's *Illustrated Guide to Machine Learning* one of its seven books precisely because it teaches "how the math actually applies to the results."
>
> **What you give up — stated plainly:** The short route omits distributional proofs and advanced concentration results. Keep conditional probability, expectation/variance and simulation of sampling uncertainty; these support honest validation and inference. MGFs and measure theory are not gates for basic confidence intervals.
>
> **Complete the core before:** [M6](2-statistics-and-data.md#module-6) inference, [M6½](2-statistics-and-data.md#module-6-half) causal work, [M9](3-classical-ml.md#module-9) or [M13](4-probabilistic-ml.md#module-13). Review job requirements using the [career guide's sampling method](../guides/career-operations.md#skills-checklist); a role title alone does not specify the necessary depth.

* **📦 Module Project (mandatory) — Monte Carlo intuition engine**
  * **Deliverable:** A simulation suite that answers four probability questions numerically *and* analytically, and shows the two converge: (1) the birthday problem, (2) the Monty Hall problem, (3) the coupon-collector expected time, (4) a random walk starting at 0 with steps ±1 at equal probability, absorbing boundaries at -10 and +10, and a recorded first-hitting time or right-boundary outcome. One module per problem, one shared `simulate(n_trials, seed)` interface.
  * **Definition of done:** (1) `pytest` suite asserting each simulated estimate lands within a stated, seed-stable tolerance of the corresponding analytic answer; for the bounded walk, test the hitting-time distribution and boundary probability rather than an unspecified closed form; (2) `README.md` with a convergence plot per problem (estimate vs `n_trials`, with the analytic value as a horizontal line); (3) a results memo explaining what the convergence rate you observed tells you about the Law of Large Numbers and the CLT.
  * **Stretch:** Add a variance-reduction technique (antithetic variates or control variates) to one problem and quantify the efficiency gain.
  * *Use the [role prerequisite inventory](../guides/practitioner-track.md#prerequisites) to decide when this core is needed. Numerical output must be accompanied by assumptions and a check against an analytic quantity.*

---

[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [🟨 Statistics & Data (M6–M8b) →](2-statistics-and-data.md)
