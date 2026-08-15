#!/usr/bin/env python3
"""Validate the interview skill's portable structure and Markdown links."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "interview"
REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "WORKSPACE.md",
    "SESSION-FORMAT.md",
    "SCORECARD.md",
    "behavioral.md",
    "system-design.md",
    "coding.md",
    "templates/SESSION.md",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for relative in REQUIRED:
        if not (SKILL / relative).is_file():
            fail(f"missing {SKILL / relative}")

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        fail("SKILL.md has no frontmatter")
    frontmatter = skill_text.split("---", 2)[1]
    for key in ("name", "description"):
        if not re.search(rf"(?m)^{key}:\s*\S", frontmatter):
            fail(f"SKILL.md frontmatter is missing {key}")
    if "disable-model-invocation: true" not in frontmatter:
        fail("SKILL.md must disable model invocation")

    openai_text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if "allow_implicit_invocation: false" not in openai_text:
        fail("agents/openai.yaml must disable implicit invocation")

    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown in [ROOT / "README.md", *SKILL.rglob("*.md")]:
        text = markdown.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "#")):
                continue
            path_text = target.split("#", 1)[0]
            if path_text and not (markdown.parent / path_text).resolve().exists():
                fail(f"broken link in {markdown.relative_to(ROOT)}: {target}")

    session = (SKILL / "templates" / "SESSION.md").read_text(encoding="utf-8")
    for heading in (
        "## Interview contract",
        "## Prompt summary",
        "## Observable evidence",
        "## Hints",
        "## Scorecard",
        "## Feedback",
        "## Next drill",
    ):
        if heading not in session:
            fail(f"session template is missing {heading}")

    print("Interview skill validation passed.")


if __name__ == "__main__":
    main()
