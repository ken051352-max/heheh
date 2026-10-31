[Home](../README.md) · [Start here](../START-HERE.md) · [← Week 0](week-0.md#week-0)

---

<a id="first-30-days"></a>
# Your first 30 days (after Week 0)

**Your one next step:** watch [CS50P Lecture 0](https://cs50.harvard.edu/python/weeks/0/), then follow [Week 1](#week-1) below.

Not done [Week 0](week-0.md#week-0) yet? Do that first. It is seven short days in your browser.

---

<a id="first-30-days-shape"></a>
## How these four weeks work

- **About 5–7 hours a week.** That is 45–60 minutes on most days. A 15-minute day still counts.
- **One main course:** Harvard's free [CS50P](https://cs50.harvard.edu/python/). You keep going with it after Day 30.
- **Small wins every week.** Each week has a goal, a short "done when" list, and one optional "math meets code" task.
- **Nothing here is a test or a gate.** The maths placement in Week 2 only helps you pick resources.

| Week | Main focus | You finish with |
|---|---|---|
| [1](#week-1) | CS50P Lecture 0 + Problem Set 0 | Your first GitHub repository, `python-journey` |
| [2](#week-2) | CS50P Lecture 1 + a maths check-in | A rough map of your maths, and a first look at vectors |
| [3](#week-3) | CS50P Lecture 2 + Exercism practice | Loops you can write without looking |
| [4](#week-4) | CS50P Lecture 3 + your first original project | A small program that is entirely yours |

<a id="skill-groups"></a>
### What these weeks build: the 4 skill groups

AI engineering needs [four groups of Python skills](../curriculum/1-foundations.md#python-skill-groups). These weeks start the first two. The other two follow straight after Day 30.

| Skill group | Weeks 1–4 | Right after |
|---|---|---|
| 1 · Core data & control flow | Weeks 1–3 (variables, conditionals, loops, functions) | CS50P Lecture 8 (reading classes) |
| 2 · APIs, JSON & error handling | Week 4 `try`/`except`, plus the optional [JSON micro-task](#week-4-json) | Weather-CLI capstone |
| 3 · File & log I/O | — | CS50P Lecture 6 (files) |
| 4 · Environments (`venv` / `uv`) | Handled for you by cs50.dev | Your first project on your own machine |

<a id="first-30-days-ai-rule"></a>
> **🚦 One rule about AI for these weeks:** ask AI to *explain* a concept or *quiz* you, never to write your code. Write it yourself, even when it's slow ([why](../curriculum/1-foundations.md#ai-usage-rule)). You unlock AI coding assistants later, by passing a [3-check gate](../curriculum/1-foundations.md#three-check-gate).

<a id="first-30-days-helpers"></a>
### Free helpers (use any time, never required)

- [Python Tutor](https://pythontutor.com/python-compiler.html): paste code and watch it run step by step. Great for confusing loops.
- [futurecoder](https://futurecoder.io/): a free interactive beginner course. Use it if a CS50P idea doesn't click.
- [Exercism Python track](https://exercism.org/tracks/python): free practice exercises with an in-browser editor.

---

<a id="week-1"></a>
## Week 1 — Your first real course and your first repository

**Goal:** move from Scrimba's playground to a real editor, and put your Week 0 work online.
**Time:** about 6 hours.

1. **Watch** [CS50P Lecture 0, Functions and Variables](https://cs50.harvard.edu/python/weeks/0/) (about 1 hour; pause and type along).
2. **Create a free GitHub account.** CS50P uses it to collect your work.
3. **Open [cs50.dev](https://cs50.dev/).** It is VS Code in your browser with Python ready. Nothing to install.
4. **Do [Problem Set 0](https://cs50.harvard.edu/python/psets/0/):** five short problems. Follow the steps at the top of that page to submit.
5. **Create a public repository called `python-journey`.** Use GitHub's [repository quickstart](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories). Upload *your* versions of PayUp, the word-scramble game and the karaoke queue manager from Week 0.
6. **Write a short `README.md`:** one line per project, saying what it does and one thing you learned.

> Keep CS50P problem-set solutions **out** of your public repository. CS50's [academic honesty rules](https://cs50.harvard.edu/python/honesty/) ask you not to share them. Your Scrimba projects and your own projects are fine to publish.

**Done when:**

- [ ] I watched Lecture 0 and submitted all five Problem Set 0 problems.
- [ ] `python-journey` is public, with my three Scrimba projects and a README.

<a id="week-1-math"></a>
**Math meets code (optional, ~20 min): how steep is y = x²?**
Type this in cs50.dev and run it. Then try `h = 0.01` and `h = 0.001`. What number does the answer approach?

```python
def f(x):
    return x ** 2

h = 0.1
print((f(3 + h) - f(3)) / h)
```

You just estimated a derivative. Calculus will later tell you the exact answer is 6.

---

<a id="week-2"></a>
## Week 2 — Decisions in code, and a friendly maths check-in

**Goal:** write programs that make choices, and get a rough picture of your maths.
**Time:** about 6–7 hours.

1. **Watch** [CS50P Lecture 1, Conditionals](https://cs50.harvard.edu/python/weeks/1/), then do [Problem Set 1](https://cs50.harvard.edu/python/psets/1/).
2. **Take Khan Academy's [Precalculus course challenge](https://www.khanacademy.org/math/precalculus/test/x9e81a4f98389efdf:course-challenge) once** (30 questions, about 30–45 minutes). It is free with an account.
   - This is **placement only, never a gate.** Whatever you score, you continue CS50P next week.
   - Write your score down. The [placement guide](../curriculum/1-foundations.md#math-diagnostic) shows which free resources fit your result.
3. **Watch** episodes 1–3 of 3Blue1Brown's [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) (about 30 minutes in total).

**Done when:**

- [ ] I watched Lecture 1 and submitted Problem Set 1.
- [ ] I took the Khan course challenge once and wrote down my score.
- [ ] I watched Essence of Linear Algebra episodes 1–3.

<a id="week-2-math"></a>
**Math meets code (optional, ~20 min): a 2×2 matrix, by hand then in NumPy.**
On paper, multiply the matrix `[[2, 1], [0, 3]]` by the vector `[1, 2]`. Then check it in cs50.dev (run `pip install numpy` first if needed):

```python
import numpy as np

A = np.array([[2, 1], [0, 3]])
v = np.array([1, 2])
print(A @ v)
```

Did you get `[4 6]` by hand? Episode 3 shows this as "moving" the vector to a new place.

---

<a id="weeks-3-4"></a>
<a id="week-3"></a>
## Week 3 — Loops, and practice that sticks

**Goal:** repeat actions with loops, and practise until they feel normal.
**Time:** about 6 hours.

1. **Watch** [CS50P Lecture 2, Loops](https://cs50.harvard.edu/python/weeks/2/), then do [Problem Set 2](https://cs50.harvard.edu/python/psets/2/).
2. **Join the free [Exercism Python track](https://exercism.org/tracks/python).** Solve three exercises in the browser editor:
   [Hello World](https://exercism.org/tracks/python/exercises/hello-world),
   [Guido's Gorgeous Lasagna](https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna) and
   [Ghost Gobble Arcade Game](https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game).
3. **Retrieval warm-up:** before each session, write last session's key idea from memory in 5 minutes.

**Done when:**

- [ ] I watched Lecture 2 and submitted Problem Set 2.
- [ ] I solved three Exercism exercises.

<a id="week-3-math"></a>
**Math meets code (optional, ~25 min): plot y = x² and estimate the slope.**
Run `pip install matplotlib`, then:

```python
import matplotlib.pyplot as plt

xs = [x / 10 for x in range(-40, 41)]
ys = [x ** 2 for x in xs]
plt.plot(xs, ys)
plt.savefig("parabola.png")
```

Open `parabola.png`. Near x = 3, how far does y rise when x moves one step right? Compare with your Week 1 answer.

---

<a id="week-4"></a>
## Week 4 — Handle errors, and build something that is yours

**Goal:** make programs that survive bad input, and ship your first original project.
**Time:** about 7 hours.

1. **Watch** [CS50P Lecture 3, Exceptions](https://cs50.harvard.edu/python/weeks/3/), then do [Problem Set 3](https://cs50.harvard.edu/python/psets/3/).
2. **Solve two more Exercism exercises** (five in total):
   [Meltdown Mitigation](https://exercism.org/tracks/python/exercises/meltdown-mitigation) and
   [Leap](https://exercism.org/tracks/python/exercises/leap).
3. **Build your first original mini project** (the [M1 starter project](../curriculum/1-foundations.md#m1-starter-project)). Pick **one**:
   - **Command-line calculator:** asks for two numbers and an operator, and handles "divide by zero" and typos politely.
   - **Number-guessing game with your own twist:** for example, a limited number of guesses, a score, or difficulty levels.
   CS50P Problem Set 4 also contains a guessing game. Give yours a different design, and never copy a pset solution.
4. **Add it to `python-journey`** with a short README section, and share the link with one person.

**Done when:**

- [ ] I watched Lecture 3 and submitted Problem Set 3.
- [ ] I have solved five Exercism exercises in total.
- [ ] My mini project is in `python-journey` with a README section.
- [ ] I shared something I built with at least one person.

<a id="week-4-math"></a>
**Math meets code (optional, ~20 min): add 1 + 2 + … + n two ways.**
Add a "sum mode" to your calculator, or write a separate script. Compute the sum with a loop, then with `n * (n + 1) // 2`. Do they always match? Wrap `int(input())` in `try`/`except` so a typo doesn't crash it. You will *prove* this formula later in [Book of Proof](https://richardhammack.github.io/BookOfProof/).

<a id="week-4-json"></a>
**APIs meet code (optional, ~20 min): your first JSON request.**
Run `pip install requests` in cs50.dev. Then fetch today's London temperature from the free, key-less [Open-Meteo API](https://open-meteo.com/):

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 51.5, "longitude": -0.12, "current": "temperature_2m"}
try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    print(response.json()["current"]["temperature_2m"])
except (requests.RequestException, KeyError) as error:
    print("Could not get the weather:", error)
```

Change the latitude to `999`. What happens, and which line catches it? This is skill group 2 in a few lines, and it previews your weather-CLI capstone.

---

<a id="first-30-days-undergrads"></a>
## If you follow the four-year plan

The [Four-Year Plan, S1](four-year-plan.md#s1) builds on exactly these weeks. Two extra items, both small:

- **End of Week 4 (10 minutes):** create your LinkedIn and Codeforces/LeetCode accounts. Don't start solving yet.
- **From Week 5:** begin easy interview problems, once CS50P Lectures 0–3 feel comfortable.

<a id="first-30-days-log"></a>
## Your daily log (one line)

After each session, write one line in a notes app or a text file:

> Today I built ___. I got stuck on ___. Next session I will ___.

The [progress tracker](progress-tracker.md#starter-tracker) has a 12-box starter version of these four weeks.

<a id="first-30-days-after"></a>
## After Day 30

- **Keep going with CS50P.** Lectures 4–9 complete [Module 1](../curriculum/1-foundations.md#module-1).
- **Your end-of-M1 capstone is the weather CLI.** Start it around CS50P Lectures 5–6, once you have seen testing and files.
- **Prefer reading to video?** The [Helsinki Python MOOC](https://programming-26.mooc.fi/) is an equally good depth option.
- **Want motivation alongside?** [Automate the Boring Stuff](https://automatetheboringstuff.com/) shows what Python can do for you every day.
- **Feeling stuck?** Use the [stuck or unmotivated table](how-to-read-a-module.md#stuck-or-unmotivated).

Why the weeks look like this: see [Why this design](week-0.md#why-this-design).

---

[Home](../README.md) · [← Week 0](week-0.md#week-0) · [Progress tracker](progress-tracker.md#starter-tracker)
