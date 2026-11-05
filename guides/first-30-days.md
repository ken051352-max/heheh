[Home](../README.md) · [Semester plan](first-semester.md#semester-plan) · [Week 0](week-0.md#week-0)

<a id="first-30-days"></a>
# First 30 days: the opening four study milestones

**Continue at [Week 1](#week-1), or the first skill you have not yet demonstrated.** [Week 0](week-0.md) is optional orientation for someone who has never run Python, not a compulsory repeat for experienced learners.

<a id="first-30-days-shape"></a>
## How this fits the semester

These are the detailed opening tasks of the [single first-semester schedule](first-semester.md#semester-plan). Its workload, readings, buffers and later milestones govern the plan. “30 days” is a familiar label, not a deadline; stretch the four milestones across more calendar weeks when college needs the time.

- Use one free lecture spine, [Harvard CS50P](https://cs50.harvard.edu/python/). Lectures, notes and problem statements are public. Hosted submission/feedback may need the course's free accounts; local work is valid roadmap evidence.
- Each week below has **one small required practice artifact** and a readiness check. Additional course problems and Exercism are optional practice for a demonstrated gap. If seeking the CS50 certificate, separately follow the course's full requirements.
- Save code, expected/actual outputs, a short explanation and the next task. A private folder, local repository or selectively shared artifact is enough. Public hosting is optional.
- Required automated tests start after Lecture 5 in [semester Week 6](first-semester.md#week-6). Manual normal/boundary checks are appropriate earlier.

<a id="skill-groups"></a>
## What grows next

**Do now:** values, functions, conditions, loops and exceptions. **Next:** imports, tests, file handling and an offline Weather CLI. **Later depth:** async, advanced typing, frameworks and deployment. These align with [M1's skill groups](../curriculum/1-foundations.md#python-skill-groups), without requiring every tool at once.

<a id="first-30-days-ai-rule"></a>
## AI and independent understanding

Attempt the small program yourself first. AI may explain a concept, ask questions or critique your attempted reasoning; keep generated solutions closed during the final changed-example check. Label assistance in your notes. Follow the [readiness policy](readiness-checks.md#how-to-check) and the course's own assignment rules. Assisted output and green tests alone do not show independent understanding.

<a id="first-30-days-helpers"></a>
## One helper when needed

[Python Tutor](https://pythontutor.com/python-compiler.html) helps trace code. [futurecoder](https://futurecoder.io/) supplies another interactive explanation. [Exercism Python](https://exercism.org/tracks/python) offers additional exercises. Pick a helper for a named difficulty and return to the weekly task; none adds a mandatory exercise count.

<a id="week-1"></a>
## Week 1 — Functions, input and a saved artifact

1. Continue [CS50P Lecture 0, Functions and Variables](https://cs50.harvard.edu/python/weeks/0/), skipping the opening examples you already demonstrated in Week 0. Pause to predict outputs.
2. In the course's [browser workspace](https://cs50.dev/) or your local Python editor, write a bill-share function accepting a total and a positive integer group size. Begin with valid numeric inputs. Separate the returned value from its display.
3. Save it in a `python-journey` folder or repository with a README saying what it does, how you ran it and one example result. Use the [beginner setup](../resources/beginner-projects/README.md#setup) when moving to local project dependencies; no install is needed to run the simple browser exercise.
4. Attempt [Python basics, tasks 1–2](readiness-checks.md#python-basics). Save your prediction before running the changed example.

**Done when:** the function returns the explained result for two valid inputs and someone can reproduce the saved example. Invalid group sizes arrive next week.

**Optional practice:** choose a matching [Problem Set 0](https://cs50.harvard.edu/python/psets/0/) exercise if input/types remain unclear. Keep course solutions private in accordance with [CS50's honesty rules](https://cs50.harvard.edu/python/honesty/). No public sharing or course submission is needed for this original artifact.

**Next:** [Week 2](#week-2). Selected book reading is in [the semester milestone](first-semester.md#week-1).

<a id="week-1-math"></a>
<details>
<summary>Later or optional: connect a function with college calculus</summary>

For `f(x) = x ** 2`, calculate `(f(3 + h) - f(3)) / h` with `h = 0.1` and then `0.01`. Compare with the derivative 6 at x = 3. Do this when college calculus makes it useful; it is not extra Week 1 work.

</details>

<a id="week-2"></a>
## Week 2 — Conditions and boundary inputs

1. Study [CS50P Lecture 1, Conditionals](https://cs50.harvard.edu/python/weeks/1/).
2. Extend the bill-share function to reject a non-positive integer group size before dividing. Choose a simple documented result for invalid input, such as `None`; exceptions come later.
3. Predict and record the results for group sizes `-1`, `0`, `1` and `2`. Complete [Python basics](readiness-checks.md#python-basics).

**Done when:** your condition treats the boundary correctly, you explain why a negative number is not an acceptable group size, and you state your invalid-input policy.

**Optional practice:** one relevant [Problem Set 1](https://cs50.harvard.edu/python/psets/1/) problem. If you want to identify a maths gap, use the optional [maths placement workflow](../curriculum/1-foundations.md#math-diagnostic) or a permitted college example. Skipping placement always allows Week 3.

**Next:** [Week 3](#week-3). Book reading remains in [the semester milestone](first-semester.md#week-2).

<a id="week-2-math"></a>
<details>
<summary>Later or optional: connect a small matrix with college algebra</summary>

Multiply `[[2, 1], [0, 3]]` by `[1, 2]` on paper. The result is `[4, 6]`. Explain each component as a row's dot product. You do not need NumPy installation to check these two arithmetic operations. Revisit [M3](../curriculum/1-foundations.md#module-3) when the topic matters in college.

</details>

<a id="weeks-3-4"></a>
<a id="week-3"></a>
## Week 3 — Loops and a hand trace

1. Study [CS50P Lecture 2, Loops](https://cs50.harvard.edu/python/weeks/2/).
2. Write a function summing a list of expense amounts; write another counting amounts at or above a chosen threshold. Use only supplied local values.
3. Trace each function on paper for three entries and an empty list. Then run it. Attempt [Loops and errors, tasks 1–2](readiness-checks.md#loops-and-errors).

**Done when:** the accumulator and count are correct for the changed example and empty input, and you can explain how the loop reaches them.

**Optional practice:** one relevant [Problem Set 2](https://cs50.harvard.edu/python/psets/2/) exercise, or one Exercism loop/list exercise. Choose based on a gap rather than adding both lists to the week's work.

**Next:** [Week 4](#week-4). Book reading: [semester Week 3](first-semester.md#week-3).

<a id="week-3-math"></a>
<details>
<summary>Later or optional: a tiny table of a quadratic</summary>

Use a loop to print `x` and `x ** 2` for `-2`, `-1`, `0`, `1`, `2`. Sketch the five points on paper. A plotting library is unnecessary for this early example.

</details>

<a id="week-4"></a>
## Week 4 — An original calculator that handles errors

1. Study [CS50P Lecture 3, Exceptions](https://cs50.harvard.edu/python/weeks/3/).
2. Read the [calculator brief and starter](../resources/beginner-projects/calculator/README.md#start). Implement the first working version, then handle malformed numbers, unsupported operators and division by zero. Follow its stages; postpone automated tests until the testing lesson if needed.
3. Retain a normal run, invalid-input runs, your README and one lesson learned. Finish [Loops and errors](readiness-checks.md#loops-and-errors).

**Done when:** your own code meets the project's starter-stage criteria and you can explain a changed example. This is the [M1 starter milestone](../curriculum/1-foundations.md#m1-starter-project), not the full module. A distinct number-guessing game meeting equivalent control-flow/error-handling evidence remains a valid alternative.

**Optional practice:** a relevant [Problem Set 3](https://cs50.harvard.edu/python/psets/3/) problem if exceptions remain unclear. Do not submit this repository's reference code as course work.

**Next:** [semester Week 5](first-semester.md#week-5). Book reading: [semester Week 4](first-semester.md#week-4).

<a id="week-4-math"></a>
<details>
<summary>Later or optional: compare a sum and a formula</summary>

For a positive integer `n`, compare a loop summing 1 through n with `n * (n + 1) // 2`. Check `n = 1` and a changed value. Numerical agreement on a few inputs is not a proof; [M0](../curriculum/1-foundations.md#module-0) introduces induction later.

</details>

<a id="week-4-json"></a>
<details>
<summary>Next, after libraries: a safe JSON preview</summary>

The Weather project uses local fixtures so no service or key is needed. After Lecture 4, load a synthetic example such as `{"current": {"temperature_2m": 12.5}}` with Python's `json` module and explain its nested values. Then remove a required key and describe the failure. Use the actual [Weather stages](../resources/beginner-projects/weather/README.md#stages) for its full contract; this tiny sketch is not real weather data.

</details>

<a id="first-30-days-undergrads"></a>
## College and career planning

Keep college maths and CS assignments as your main parallel courses. Save specific [equivalence evidence](readiness-checks.md#college-equivalence) instead of repeating the same material. The [India undergraduate path](india-undergraduate-path.md) and [four-year plan](four-year-plan.md#s1) use this same opening sequence. Career accounts, interview-problem quotas and choosing a job title are not first-month completion requirements.

<a id="first-30-days-log"></a>
## A note you can resume from

> Task ___. Artifact ___. Expected/actual result ___. Help used ___. Next specific action ___.

Keep the note private by default. Use the [tracker](progress-tracker.md#starter-tracker) for state and the [six-week pilot](study-pilot.md) if you want structured feedback on pacing and confusing instructions.

<a id="first-30-days-after"></a>
## After the opening four milestones

Continue at [semester Week 5](first-semester.md#week-5): libraries, tests, files and the Weather CLI, with scheduled buffers. Keep M1 active until its [core evidence](readiness-checks.md#m1-ready) is demonstrated. If you need more time, use [recovery](first-semester.md#recovery); do not add SQL or restart onboarding merely because 30 days elapsed.

[Home](../README.md) · [Semester Week 5 →](first-semester.md#week-5) · [Readiness](readiness-checks.md) · [Tracker](progress-tracker.md#starter-tracker)
