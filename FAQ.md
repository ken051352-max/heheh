[🏠 Roadmap home](README.md) · [🧭 Start here](START-HERE.md)

---

# ❓ Frequently Asked Questions

Short answers to the questions people actually ask on first contact. If your question is about *how to
use* a module rather than *what this repo is*, see [How to read a module](guides/how-to-read-a-module.md).

**Jump to:** [The basics](#basics) · [Structure](#structure) · [Using it](#using-it) · [Time & difficulty](#time) · [Symbols](#symbols) · [Contributing](#contributing)

---

<a id="basics"></a>
## The basics

### What is this repository?

A free, self-study curriculum for data science and AI. It tells you which courses to take, which books
to read, and which projects to build, in what order.

### Is there code to run or software to install?

Reading the roadmap needs only a browser. It also includes optional executable practice resources: the [NumPy harness](resources/numpy-from-scratch/README.md), [local causal/data labs](resources/local-labs/README.md) and [agent-contract lab](resources/agent-lab/README.md). Their READMEs explain dependencies and commands. Build your own project artifacts as you progress.

### Do I need to clone or fork it?

Neither is required; reading it on GitHub is enough. **Fork** it if you want to use the
[progress tracker](guides/progress-tracker.md) as your personal checklist, which is the intended use.

### Who is it for?

Beginners who want a complete path, analysts moving into data science, engineers moving into ML or AI
engineering, and anyone preparing for graduate-level ML. See [Who this is for](README.md#who-this-is-for).

<a id="cost-and-access"></a>
### Does it cost anything?

**Lectures have a free route; books may be paid.** The recommended principal books are chosen for educational quality, not price. The [catalogue](resources/books.md) distinguishes paid books, authorized free text and sample/code-only access. Read selected sections as needed; Week 0 needs no purchase.

Accounts, course grading, certificates and hosted compute have separate terms. Core projects have small local routes; paid APIs, cloud/GPU scale and certificates are extensions. See [access details](guides/how-to-read-a-module.md#access-audit-table).

### I'm a first-year BTech student in India. Which role should I choose for an international career?

Keep the shared CS, mathematics, Python and data foundation broad, then explore analysis, modeling and software/application work through small projects. Choose a provisional route after feedback and revisit it each semester. The [undergraduate guide](guides/india-undergraduate-path.md) distinguishes global-company India roles, relocation and country-restricted remote roles. Current job descriptions cannot establish the best role at graduation; a roadmap improves preparation without guaranteeing employment or work authorization.

### Is it affiliated with a university?

No. It synthesises **publicly-available syllabi** from universities including MIT, Harvard, Stanford,
Cambridge, and IIT Madras into one prerequisite-ordered sequence. All course material remains the
property of those institutions. There is no credential, no enrolment, and no accreditation here.

---

<a id="structure"></a>
## Structure

### Why do the modules skip 19 and 20? Is something missing?

**Nothing is missing.** M19 and M20 existed in earlier versions and were reorganised: old M19 (MLOps)
grew into the current [M24](curriculum/6-frontier-production.md#module-24), and old M20 (Capstone) became
[M26](curriculum/6-frontier-production.md#module-26). Their numbers were deliberately left vacant so that
existing external links and bookmarks to M0–M18 keep working. Renumbering would have broken every
inbound deep link for a purely cosmetic gain. The same reasoning explains **M6½** and the **M8a / M8b**
split — these were inserted between existing modules rather than pushing every later number up by one.

### So how many modules are there really?

**27.** They are numbered M0–M18, M21–M26, plus M6½, with M8 split into M8a and M8b. The count is
27 distinct modules, not 27 consecutive numbers. Full list: [curriculum index](curriculum/README.md).

### What is in each top-level folder?

| Folder | Contents | Read it when |
| :--- | :--- | :--- |
[`curriculum/`](curriculum/) | The 27 module specifications, in six stratum pages | Constantly — this is the curriculum |
| [`guides/`](guides/) | How to read a module, fast lane, career ops, progress tracker, sources | Early and often |
| [`resources/`](resources/) | Books, toolchain, practice harnesses and local labs | When you reach the relevant module |
| [`coursepages/`](coursepages/) | Extra scaffolding for the newest modules (M6½, M8b, M21–M25) | Only when you reach those modules |
| [`audit/`](audit/) | Link-verification and fact-checking logs | Basically never, unless you doubt a claim |
| [`tools/`](tools/) | The internal link checker | Only if contributing |
| [`assets/`](assets/) | Banner images and the script that generates them | Only if contributing |

### Why are the module pages so long?

They are **reference documents**, not scripts to be read start to finish. The "Exhaustive Topic List" in
particular exists so you can (a) verify your chosen course covers the material and (b) revise before
interviews. Nobody reads it linearly. See [the anatomy of a module](guides/how-to-read-a-module.md).

---

<a id="using-it"></a>
## Using it

### Where do I actually start?

New to Python: [Week 0](guides/week-0.md#week-0), seven short days in your browser. Then the [first 30 days](guides/first-30-days.md#first-30-days). Everyone else: [START-HERE.md](START-HERE.md#other-entry-points).

### There are hundreds of links. Which resource do I pick?

Use the [Pick-One table](guides/how-to-read-a-module.md#pick-one) — one default learning route per
module, paired with its recommended principal book. Lectures are selected for free access; books can be paid and are labeled. Account/exercise terms are recorded separately.
The other links are alternatives for when a default does not suit you, and insurance against link rot.
**A module's resource list is a menu, not a to-do list.**

### Do I have to do all 27 modules?

**No,** and you should not by default. Pick a target role in
[Choose your track](README.md#choose-your-track) and do that track's module set. Only the research /
PhD-prep track uses nearly everything.

### Can I skip the mathematics?

Yes, with a stated cost. The maths-heavy modules each carry an **⚡ Intuition-First Alternative** callout
naming exactly what you give up and when you will need to come back. The
[Practitioner fast lane](guides/practitioner-track.md) is the fully sequenced version of that route.
You can validate application behavior experimentally without completing all advanced proofs. Return to the relevant mathematics when interpreting estimators, diagnosing failure or assessing theoretical claims. The application subsets do not certify the full training or mathematical modules.

### Do I have to build the projects?

Yes: complete the core artifact before claiming the competence a dependent module needs. Independent modules may proceed in parallel. Use tests for code, worked checks for mathematical/analytical work, a readable `README.md` and an honest results memo. Store it in a private local repo,
private remote repo, or selectively shared repo, or publish a carefully sanitized showcase. Public
publishing is optional: scrub API keys, credentials, private data, proprietary material, and PII first.
A private artifact proves completion to you; an external employer needs an accessible signal such as a
sanitized release or live demo. A single evolving longitudinal project (like the [Portfolio Spine](guides/portfolio-spine.md#portfolio-spine)) may satisfy multiple module outcomes when its git release tags and module mapping make each milestone reviewable. See [the enforcement rule](curriculum/README.md#module-projects).

### Can I do modules out of order or in parallel?

Respect the **Strict Prerequisites** line in each module and you can otherwise arrange things freely.
Running a maths module in parallel with a programming module is a common and effective pattern.

### What does "Video 1 (05:05)" mean?

The [source key](guides/sources.md#citation-key) preserves historical video/article shorthand with links and descriptions of its earlier use. This pass did not revalidate every video or timestamp; current technical requirements cite primary documentation.

---

<a id="time"></a>
## Time & difficulty

<a id="how-long"></a>
### How long does this take?

Estimate from your own pace. Choose one core route and a weekly budget, study for four weeks, then use the work completed to plan the next milestone. A useful planning formula is:

```text
weeks = estimated remaining focused hours / sustainable focused hours per week
```

The hour estimate is uncertain: include time for exercises, failed experiments, review and breaks, and revise it regularly. Course duration, a completed portfolio and finding employment are different outcomes. The [four-year plan](guides/four-year-plan.md) is an adaptable undergraduate schedule; the [role routes](guides/practitioner-track.md) define smaller scopes. No timeline here promises employment.

### Is it beginner-friendly?

The entry route starts gently, with stated prerequisites for later work. Resources include university courses and specialist author/community teaching, with different levels of difficulty. If you are new to programming, start with
[Week 0](guides/week-0.md#week-0) and the [first 30 days](guides/first-30-days.md#first-30-days):
one beginner course, small daily wins, and no gates. The
[Microsoft companion curricula](guides/companion-curricula.md) are optional extra practice later.

### I'm stuck / demoralised. Is that normal?

A prerequisite gap, fatigue, an unclear explanation or too much scope can all cause difficulty. Identify one small obstacle, revisit the needed concept or use a companion explanation. For passive-study habits, try the practice protocol in
[Module 1](curriculum/1-foundations.md#module-1).

---

<a id="known-limitations"></a>
## Known limitations

Honest notes on what is still rough. None of them block a beginner from starting [Week 0](guides/week-0.md#week-0).

- **The old 15-question maths diagnostic was never written.** It has been replaced by the active, free, non-gating [maths placement workflow](curriculum/1-foundations.md#math-diagnostic). The historical six-strand table and old status lines are kept collapsed purely as non-operational archival references for provenance (its MIT 18.01A exam and Velleman §1.5 links are retired/broken); it does not establish placement thresholds or gating cutoffs.
- **Links move.** Course providers change URLs and editions (Scrimba and the Helsinki MOOC both did in 2026). The [current audit](audit/overhaul-2026-11-05.md) distinguishes content inspected, checks executed and unresolved access; historical HTTP logs do not establish current availability.
- **Access can change.** Free lecture access is distinct from grading, certificates and hosted services. Paid books are intentional recommendations, labeled by edition and access. Report a paid-only default lecture or a wrong access label.
- **Advanced modules are dense.** Later modules keep university-level depth, much of it collapsed under "Advanced / later". Use the [Pick-One table](guides/how-to-read-a-module.md#pick-one) and skip what you don't need yet.
- **Found something contradictory?** [Open a "Something was confusing" issue](https://github.com/akazadivu-design/data-sci/issues/new/choose) upstream. If you couldn't work out what to do, that is a defect in the roadmap, not your mistake.

---

<a id="symbols"></a>
## Symbols

These marks appear next to links and claims throughout the repository.

| Symbol | Meaning |
| :--- | :--- |
| ✅ | Completion or historical check marker; consult the associated dated evidence before treating it as current verification |
| ⚠️ | Access or behavior needs review; an automated refusal does not establish browser accessibility |
| ❌ | Failed check at the recorded date; inspect the cause before replacing a resource |
| 🔁 | The original URL broke and was replaced with a verified alternative |
| ⏭ | Deliberately deferred to a later release |
| 📦 | A mandatory module project |
| ⚡ | An intuition-first alternative route for the practitioner track |
| 🩺 | The maths placement (optional, never a gate) |
| 🟩 🟨 🟧 🟦 🟪 🔴 | The six curriculum strata, in order |

---

<a id="contributing"></a>
## Contributing

### Can I contribute?

Yes — corrections, dead-link reports, and resource updates are welcome, and you don't need to be an
expert. Reporting a single dead link is a real contribution. See [CONTRIBUTING.md](CONTRIBUTING.md)
for the resource bar and the [code of conduct](CODE_OF_CONDUCT.md) for expected behaviour.

### I found a broken link.

Open an issue using the **Dead or moved link** template — it prompts for the URL, the file it appears
in, and what you saw. Or open a PR replacing it with a verified alternative. Run
`python3 tools/check_links.py` before submitting to confirm internal links still pass.

### The docs confused me. Is that worth reporting?

Yes. There is a **Something was confusing** issue template for exactly this. If you couldn't work out
what to do, the signposting failed — that is a defect, not your mistake.

### What licence is this under?

[CC BY-SA 4.0](LICENSE.md). You may share and adapt it, including commercially, with attribution and
under the same licence. Note this covers **this repository's own text and images** — linked course
material belongs to its respective institution.

---

**Question not answered here?** Open an issue. If it is a question about first contact with the repo,
it belongs on this page and the answer will be added.

---

[🏠 Roadmap home](README.md) · [🧭 Start here](START-HERE.md) · [📖 How to read a module](guides/how-to-read-a-module.md)
