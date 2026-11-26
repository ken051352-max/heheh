# Private progress and realistic planning

Use the standard-library helper at `scripts/progress.py`, relative to this skill. Pass the validated roadmap checkout as `--root`. Python 3.12+ matches this repository's toolchain. No model API, network or package installation is needed for persistence.

```text
python <skill-dir>/scripts/progress.py --root <checkout> init
python <skill-dir>/scripts/progress.py --root <checkout> status
python <skill-dir>/scripts/progress.py --root <checkout> plan --file <private-plan.json>
python <skill-dir>/scripts/progress.py --root <checkout> record --file <private-session.json>
```

These angle-bracket values are placeholders, not literal shell syntax. Quote paths containing spaces. Write UTF-8 JSON payloads with file tools, not shell interpolation of learner text. Keep payloads under `study-private/tutor/`; the tool's state is `study-private/tutor/state.json`. `init` is idempotent and starts with no sessions or plan. The initial timezone is Asia/Kolkata and role focus undecided; these are context defaults, not assessed skills. Do not initialize/save when the learner opts out.

Read `status` first. It is a summary, so inspect the relevant entries in `state.json` when you need actual evidence, assistance or prior attempts. An absent record means unknown progress; `init` may create an empty record. Other errors are not permission to reset. A corrupt file, a redirected storage path or an existing `state.lock` requires inspection. Preserve the state and `state.previous.json`; do not delete a lock while another session may be writing. The helper uses a lock, validation and atomic replacement for local writes; this is not a cloud backup or protection from every filesystem failure.

## A plan the learner can actually use

Use current available time, college deadlines and the last demonstrated skill. Clarify missing availability before saving a weekly commitment; meanwhile propose a small session and label any estimate. The plan's `week_start` starts a seven-day window and need not be Monday. Tasks plus buffer must fit within `available_minutes`. Buffer size and study/review split are adjustable design choices, not scientifically optimal constants.

Example shape only — substitute the learner's agreed plan before saving:

```json
{
  "week_start": "2026-11-09",
  "available_minutes": 120,
  "buffer_minutes": 30,
  "tasks": [
    {
      "id": "m1-functions-practice",
      "module_id": "M1",
      "task": "Explain return versus print, then change a bill-share function",
      "minutes": 45,
      "reference": "guides/first-semester.md#week-1",
      "readiness_check": "guides/readiness-checks.md#python-basics (tasks 1–2)"
    },
    {
      "id": "m1-functions-transfer",
      "module_id": "M1",
      "task": "Predict two changed inputs and explain the result independently",
      "minutes": 45,
      "reference": "guides/first-semester.md#week-1",
      "readiness_check": "guides/readiness-checks.md#python-basics (tasks 1–2)"
    }
  ]
}
```

Save plans only when they reflect the learner's requested/accepted schedule, not as completed work. Replacing a plan preserves sessions; the previous state contains the immediately preceding version. Keep an important older plan in the private pilot notes before replacing it. The helper checks shape, IDs and budget; the tutor must check that references exist, prerequisites fit and the task is appropriately sized.

On a short day, reduce to one behavior or explanation. After missed weeks, use the last artifact, a brief changed example and a specific repair if needed. Preserve earlier evidence, defer new scope and do not count missed sessions as hours owed. At a weekly review, compare estimated and known actual time for comparable tasks; show missing-time records separately. Distinguish access problems, unclear instructions, knowledge gaps and life constraints in the private pilot reflection. Adjust scope before accumulating more courses. The six-week pilot is the existing feedback process; do not create a second semester schedule.

## Record evidence, not inferred mastery

One record describes one capability attempted during a session. If splitting a session into several records, allocate time once across them or use `null`; never repeat the full duration in each record. Minutes are actual learner-reported/measured study time, not chat elapsed time or the plan estimate.

Example shape only — never insert this example as actual progress:

```json
{
  "id": "2026-11-09-functions-01",
  "date": "2026-11-09",
  "module_id": "M1",
  "capability": "functions-return",
  "task": "Explain return versus print",
  "minutes": null,
  "artifact": "study-private/python-journey/share.py",
  "evidence": "Learner reports that they ran the example with a hint; independent transfer is pending.",
  "evidence_source": "learner-report",
  "assistance": "hints",
  "understanding": "assisted",
  "next_action": "Open the saved function and predict its returned value for two new inputs before running it.",
  "review_after": "2026-11-12"
}
```

- `module_id`: actual manifest module/subset ID. Keep a stable short `capability` name for subsequent reviews of the same skill.
- `artifact`: path or reference, or `null` when none exists. Store only needed evidence; for an oral explanation, save a brief factual note rather than a fabricated code artifact.
- `evidence_source`: `learner-report` or `tutor-observed`. A tutor observing code output did not necessarily observe independent authorship.
- `assistance`: `none`, `hints`, `solution` or `mixed` for that attempt.
- `understanding`: `not-attempted`, `assisted`, `independent` or `needs-review`. Use `independent` only with concrete evidence and an artifact for a changed attempt without solution copying. If a later independent attempt follows an assisted one, record the new attempt separately.
- `review_after`: optional date or `null`. Agree a useful revisit based on difficulty, retention and availability; no fixed universal interval. `status --as-of YYYY-MM-DD` inspects a specific date without changing records.

Reuse the same event ID when retrying an identical write. An identical record is a no-op; a conflicting ID is rejected. On conflict, inspect the saved event rather than silently assigning a new ID and duplicating time. For a genuine later attempt, use a new ID. For a correction, keep the original record and explain the correction in a new evidence note without inventing more study minutes; inaccurate time totals require an explicit reviewed state correction, not a negative entry.

Status sums known minutes, lists unknown-duration records separately, and returns due reviews using the latest dated record for each module/capability. Same-date ties follow saved order. This queue suggests what to revisit; it does not run an optimal memory algorithm or certify competence. An independent attempt can still need a later review. A plan older than its seven-day window needs replanning, not automatic rollover.

Keep the human tracker consistent when the learner asks to update it; do not automatically mark curriculum modules complete. For college-equivalence evidence, record the concrete capability, artifact and what was independently explained, then apply the roadmap's waiver guidance.

No background notifications are installed. Show due reviews when a session resumes. If reminders are requested, distinguish a suggested calendar entry from an actual configured scheduler and do not claim delivery without creating and verifying one through available authorized tools.
