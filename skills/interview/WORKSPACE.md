# Workspace

The workspace is where candidate-owned state lives. Resolve it in this order:

1. A path explicitly supplied in the current invocation.
2. The `workspace` value in `.interview/config.yaml` found from the current
   directory.
3. The current working directory.

Resolve relative configured paths from the directory containing
`.interview/config.yaml`. Confirm before writing outside the current directory.
A minimal alternate configuration is:

```yaml
workspace: ../interview-prep
```

Do not require a parser or add configuration fields without a current need.

## First run

Explain the intended writes, obtain confirmation, then create only missing
paths:

```text
RESUME.md                         # optional until supplied by the candidate
.interview/
  config.yaml
  PROFILE.md
  TARGET.md
  PLAN.md
  STORY-BANK.md
  PROGRESS.md
  QUESTION-BANK.md
  NOTES.md
  sessions/
  artifacts/
    coding/
    system-design/
```

Copy the adjacent [templates](templates/) rather than improvising formats.
Preserve existing files and user prose. Use the next four-digit sequence for
session names: `NNNN-YYYY-MM-DD-<track>.md`; use `mixed` for mixed sessions.

Resume-dependent work includes behavioral resume deep dives and resume review.
If `RESUME.md` is missing, offer exactly these paths forward: provide an
existing file path, paste content to create it, or continue without it. Do not
create an empty resume without consent. Coding and system-design sessions can
continue independently.

Read only preparation files needed for the chosen session. Treat resume,
profile, answers, and evaluations as sensitive. State is committed normally;
tell users they may gitignore `.interview/` and/or `RESUME.md`, but never edit
`.gitignore` unless asked.

## State updates

- `PROFILE.md`: stable candidate context and preferences; do not infer protected
  or personal attributes.
- `TARGET.md`: desired role, level, process, and confirmed company information.
- `PLAN.md`: current priorities and scheduled drills.
- `STORY-BANK.md`: candidate-supplied stories and evidence; never fabricate.
- `PROGRESS.md`: aggregate only from cited sessions; retain contradictory data.
- `QUESTION-BANK.md`: original or user-supplied prompts and repetition status.
- `NOTES.md`: candidate-owned scratch notes; do not silently rewrite.

Ask before replacing content. Prefer narrow append/update operations after each
recorded session.
