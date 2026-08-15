# Skills

Reusable agent skills for developers.

## Interview

`/interview` is a stateful software-engineering interview gym for behavioral, system-design, and coding interviews. It adapts to the candidate's experience, resume, target role, and preferred language; conducts realistic mock interviews; provides evidence-based coaching; and records progress between sessions.

### Install for GitHub Copilot

GitHub Copilot is the primary supported host. With GitHub CLI 2.90.0 or later:

```bash
gh skill preview chasehelton/skills interview
gh skill install chasehelton/skills interview --agent copilot --scope project
```

You can also copy `skills/interview` into `.github/skills/interview`, `.agents/skills/interview`, or `.claude/skills/interview` in a project.

### Install for Claude Code

```bash
gh skill install chasehelton/skills interview --agent claude-code --scope project
```

Then invoke it explicitly:

```text
/interview
/interview mock behavioral
/interview practice coding graphs
/interview review progress
```

### Install for Codex and compatible Agent Skills clients

Install with the host's Agent Skills installer, use GitHub CLI if the host is offered by `gh skill install`, or copy `skills/interview` into the host's supported skills directory.

### Validate

```bash
gh skill publish --dry-run
```

## Philosophy

These skills are operating procedures, not prompt dumps. They use concise entry points, progressive disclosure, explicit completion criteria, and durable workspace state.

## License

MIT
