# Skills

Reusable agent skills for developers.

## Interview gym

`/interview` is a stateful software-engineering interview gym for behavioral, system-design, and coding interviews. It adapts to the candidate's experience, resume, target role, and preferred language; conducts realistic mock interviews; provides evidence-based coaching; and records progress between sessions.

### Install for GitHub Copilot

GitHub Copilot is the primary acceptance target. Install the canonical
[`skills/interview`](skills/interview/SKILL.md) directory using your client's skill
installer, or copy it into a supported project skill directory:

```bash
mkdir -p .github/skills
cp -R /path/to/repo-root/skills/interview .github/skills/interview
```

Restart or reload Copilot, then invoke `/interview` explicitly. Clients that
support repository-based installation may install `chasehelton/skills` and select
the `interview` skill instead.

### Install for Claude Code

```bash
mkdir -p .claude/skills
cp -R /path/to/repo-root/skills/interview .claude/skills/interview
```

### Install for Codex and compatible clients

```bash
mkdir -p .agents/skills
cp -R /path/to/repo-root/skills/interview .agents/skills/interview
```

Use the skill directory expected by your client if it differs. The portable core
uses standard `name` and `description` frontmatter; `agents/openai.yaml` disables
implicit invocation for compatible OpenAI clients.

### Use

```text
/interview
/interview mock behavioral
/interview mock system-design
/interview mock coding
/interview mock mixed
/interview practice behavioral impact
/interview practice coding graphs
/interview review resume
/interview review progress
```

With no arguments, the interviewer asks only the focused questions needed to
establish the **interview contract**. Mock feedback is held until the end unless
you opt into live feedback.

The first run creates state in the directory where you invoke the skill. Put a
`RESUME.md` there for resume-grounded sessions. You may configure another
workspace; see [WORKSPACE.md](skills/interview/WORKSPACE.md).

### State and privacy

Generated state is ordinary project content by default:

- `RESUME.md` can contain sensitive personal information.
- `.interview/` contains answers, evaluations, and preparation notes.
- Review both before sharing or committing them.
- Gitignore either path if you want local-only state. The skill never edits
  `.gitignore` unless asked.

## Philosophy

Attempt before instruction. Mock interviews measure independent performance;
practice sessions teach; review sessions synthesize. Feedback cites observable
behavior, avoids fake precision, and ends with a concrete drill. Starter prompts
are original—not a scraped proprietary question bank. See
[example prompts](skills/interview/examples/original-prompts.md).

### Validate

No dependencies are required:

```bash
python3 scripts/validate-skill.py
```

## License

[MIT](LICENSE)
