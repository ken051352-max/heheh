[Home](README.md) · [This semester](guides/first-semester.md#semester-plan) · [Resume](guides/progress-tracker.md#resume)

# Your roadmap tutor

Ask the tutor to explain a concept, help debug your attempt, check understanding or choose a task that fits your day. It reads this roadmap and can keep a **private study record shared by Codex and OpenCode**. The tutor is optional; the free lecture route and ordinary tracker still work without it. Your chosen AI tool's existing pricing and access apply.

## Start a session

In **Codex**, use the skill by name:

```text
$roadmap-tutor I have 25 minutes. Help me find my current milestone and practise one useful thing.
```

In **OpenCode v2**, select the **roadmap-tutor** primary agent in the agent picker, or load the skill in your current agent:

```text
@roadmap-tutor I missed two weeks. Read my progress and help me resume without restarting.
```

Open a new session after installation if the skill list was already loaded. The tutor should ask only what it needs, such as your available time or last attempted task. It should not invent a starting level or require a maths test before Python.

## What you can ask

- **Understand:** “Explain return versus print, then let me try a changed example.”
- **Get unstuck:** “Here is my function, expected output and actual error. Give me a small hint first.”
- **Ask directly:** “I need a worked example, then a similar problem to solve myself.”
- **Plan:** “I have three 40-minute sessions this week and exams on Friday. Plan around that with a buffer.”
- **Resume:** “Show my last next action and any reviews due. I only have 15 minutes today.”
- **Check:** “Review this artifact against M1 readiness. Separate what I demonstrated from what I did with help.”
- **Reflect:** “Compare my planned and recorded study time. What should I reduce next week?”
- **Explore:** “I am undecided about roles. Suggest one experiment after my current prerequisites.”

It uses the [semester plan](guides/first-semester.md#semester-plan), [readiness checks](guides/readiness-checks.md#how-to-check), [project briefs](resources/beginner-projects/README.md) and [current manifest](curriculum/modules.json). It can teach later modules when you reach their prerequisites. It does not need to assign every resource or turn Google, Apple or Anthropic into a promised outcome.

## Time and progress

Tell it your real availability; the roadmap's weekly estimate is only a starting assumption. The tutor keeps planned minutes separate from actual reported/measured time. Unknown time stays unknown. After a session it records the artifact, assistance, demonstrated capability, remaining gap and exact next action. A lecture watched, green reference tests or an AI-written answer does not automatically complete a module.

Records live in `study-private/tutor/state.json` in your roadmap checkout. That directory is Git-ignored, not encrypted. The helper retains the previous state as `state.previous.json`; back up important notes yourself. Both tools use this same file, so progress can survive closing a chat or reinstalling the skill. It is not a cloud account or cross-device sync. You can say “do not save this session” and keep a manual [resume note](guides/progress-tracker.md#resume) instead.

Use the existing [six-week pilot](guides/study-pilot.md#start) for reflections about access problems, confusing instructions, missing knowledge or life constraints. The tutor can help adapt your plan from those observations. Review dates appear when you return; **this installation does not send background reminders**.

## Install or update

From a local checkout with Python 3.12+, run:

```text
python tools/install_tutor.py
```

This installs the Codex skill at `~/.agents/skills/roadmap-tutor/`, an identical OpenCode copy at `~/.config/opencode/skills/roadmap-tutor/`, and the OpenCode primary agent at `~/.config/opencode/agents/roadmap-tutor.md`. It binds both copies to this checkout using local `local.json` files. It does not change model/provider configuration or permissions. If your OpenCode configuration directory is customized, the installer requires an explicit destination; see `--help`.

The installer uses each tool's documented skill directory and keeps the copies identical. OpenCode can also discover `.agents`; when both exist, its native directory takes precedence for the same skill ID. Progress remains in one checkout file. Allow OpenCode's service to finish startup before checking its skill list; an immediate isolated API request can return only built-in skills.

To update after changing the versioned tutor, use `python tools/install_tutor.py --update`. Changed destination files are backed up before replacement. Learner state remains in the checkout. To use another copy of the roadmap, run the installer there with `--update`; when already inside a valid checkout, the tutor prefers that checkout. Verify that it names the intended progress location before continuing.

[AGENTS.md](AGENTS.md) supplies automatic repository guidance. This singular `agent.md` is the user guide; it is not an automatically loaded agent definition. The reusable [skill source](resources/tutor/roadmap-tutor/SKILL.md) and [OpenCode definition](resources/tutor/opencode-agent.md) are versioned here for review.

## Maintainer checks

```text
python -m unittest discover -s tools/tests -v
python tools/check_links.py
python tools/check_curriculum.py --check
```

The progress helper uses only the standard library. See its [schema and operating guidance](resources/tutor/roadmap-tutor/references/progress-and-planning.md). Research sources and the actual installation/validation results are in the [tutor work record](audit/tutor-2026-11-05.md).
