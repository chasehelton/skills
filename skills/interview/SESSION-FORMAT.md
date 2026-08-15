# Session format

Write `.interview/sessions/NNNN-YYYY-MM-DD-<track>.md` from
[`templates/SESSION.md`](templates/SESSION.md). A record contains:

1. Date, status, and source prompt identifier—not proprietary prompt text.
2. The complete interview contract.
3. A concise prompt summary and coverage.
4. Observable evidence: candidate questions, decisions, code/design behavior,
   tests, follow-ups, timing events, and exact short excerpts when useful.
5. Every hint with its ladder level; use `None` when no hint was given.
6. Overall signal, confidence, dimension scores, and evidence for every score.
7. Feedback in **evidence → consequence → next move** form.
8. Zero to three priority improvements and one concrete next drill.

Do not claim a verbatim transcript unless one was captured. Label summaries as
summaries. Do not store hidden chain-of-thought; record observable evidence and
concise evaluation rationale only.

## Aggregate updates

After writing the session:

- Link its relative path from `PROGRESS.md`.
- Update a competency only when the record contains evidence.
- Prefer trends over averaging scores; do not manufacture decimals.
- Add the next drill to `PLAN.md`.
- Add or revise candidate-owned stories only with the candidate's facts.
- Mark prompt use in `QUESTION-BANK.md` when applicable.

**Record is incomplete** if any score lacks evidence, more than three
improvements are selected, or the next drill does not specify what to practice
and what success looks like.
