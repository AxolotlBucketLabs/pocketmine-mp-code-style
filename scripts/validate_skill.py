#!/usr/bin/env python3
"""Validate the structure, routing links, and CI policy of this Codex skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_NAME = "pocketmine-mp-code-style"
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|REPLACE_ME|YOUR_[A-Z_]+)\b")
LINK_RE = re.compile(r"\]\(((?:references|examples)/[^)#]+)(?:#[^)]+)?\)")
ACTION_USE_RE = re.compile(
    r"^\s*uses:\s*([^\s]+)@([^\s#]+)(?:\s+#\s*(.*?))?\s*$"
)
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE_RE = re.compile(r"`+[^`\n]+`+")
FORBIDDEN_PROSE_RE = re.compile(r"[—–;“”‘’]")
LOWERCASE_BULLET_RE = re.compile(r"^\s*[-*+]\s+[a-z]")
LABEL_PROSE_RE = re.compile(
    r"^\s*(?:Status|Result|Verification|Notes|Reason|Output|Summary)\s*:\s+\S"
)
RESEARCH_CONTEXT_RE = re.compile(
    r"(?i)\bPoggit\b|992c5ba4211252d202d8d4e8aac080c6|pasted text"
)
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
VERSION_COMMENT_RE = re.compile(r"^v[0-9]+(?:\.[0-9]+){0,2}(?:[-+][0-9A-Za-z.-]+)?$")
MUTABLE_ACTION_REFS = {"HEAD", "develop", "dev", "latest", "main", "master"}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def markdown_files(skill_dir: Path) -> list[Path]:
    files = [skill_dir / "README.md", skill_dir / "SKILL.md", skill_dir / "AGENTS.md"]
    files.extend(sorted((skill_dir / "references").glob("*.md")))
    files.extend(sorted((skill_dir / "examples").glob("*.md")))
    return files


def validate_workflows(skill_dir: Path) -> None:
    workflow_dir = skill_dir / ".github" / "workflows"
    if not workflow_dir.is_dir():
        fail(".github/workflows is missing")

    workflows = sorted((*workflow_dir.glob("*.yml"), *workflow_dir.glob("*.yaml")))
    if not workflows:
        fail(".github/workflows has no workflow files")

    for workflow in workflows:
        for line_number, line in enumerate(workflow.read_text(encoding="utf-8").splitlines(), 1):
            match = ACTION_USE_RE.match(line)
            if match is None:
                continue

            action, reference, version_comment = match.groups()
            if action.startswith("./"):
                continue
            if reference in MUTABLE_ACTION_REFS:
                fail(f"{workflow.name}:{line_number} uses mutable action ref {reference}")
            if FULL_SHA_RE.fullmatch(reference) is None:
                fail(f"{workflow.name}:{line_number} must pin {action} to a full commit SHA")
            if version_comment is None or VERSION_COMMENT_RE.fullmatch(version_comment.strip()) is None:
                fail(f"{workflow.name}:{line_number} needs a version comment beside {action}")


def validate_dependabot(skill_dir: Path) -> None:
    dependabot_file = skill_dir / ".github" / "dependabot.yml"
    if not dependabot_file.is_file():
        fail(".github/dependabot.yml is missing")

    dependabot_text = dependabot_file.read_text(encoding="utf-8")
    if re.search(r"^\s*-\s*package-ecosystem:\s*github-actions\s*$", dependabot_text, re.MULTILINE) is None:
        fail(".github/dependabot.yml must update GitHub Actions")
    if re.search(r"^\s*directory:\s*/\s*$", dependabot_text, re.MULTILINE) is None:
        fail(".github/dependabot.yml must monitor the repository root")


def validate_markdown_fences(skill_dir: Path) -> None:
    for markdown_file in markdown_files(skill_dir):
        open_fence: tuple[str, int, int] | None = None
        for line_number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), 1):
            match = FENCE_RE.match(line)
            if match is None:
                continue

            fence, suffix = match.groups()
            marker = fence[0]
            length = len(fence)
            if open_fence is None:
                open_fence = (marker, length, line_number)
                continue

            open_marker, open_length, open_line = open_fence
            if marker != open_marker or length < open_length or suffix.strip():
                continue
            open_fence = None

        if open_fence is not None:
            marker, length, line_number = open_fence
            fail(
                f"{markdown_file.name}:{line_number} has an unclosed "
                f"{length}-character {marker} Markdown fence"
            )


def validate_prose_style(skill_dir: Path) -> None:
    for markdown_file in markdown_files(skill_dir):
        in_fence = False
        fence_marker = ""
        fence_length = 0
        for line_number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), 1):
            fence_match = FENCE_RE.match(line)
            if fence_match is not None:
                fence, suffix = fence_match.groups()
                marker = fence[0]
                length = len(fence)
                if not in_fence:
                    in_fence = True
                    fence_marker = marker
                    fence_length = length
                elif marker == fence_marker and length >= fence_length and not suffix.strip():
                    in_fence = False
                continue

            if in_fence or line.startswith(("    ", "\t")):
                continue

            prose = INLINE_CODE_RE.sub("", line)
            if FORBIDDEN_PROSE_RE.search(prose):
                fail(f"{markdown_file.name}:{line_number} contains forbidden prose punctuation")
            if LOWERCASE_BULLET_RE.match(prose):
                fail(f"{markdown_file.name}:{line_number} starts a bullet with lowercase prose")
            if LABEL_PROSE_RE.match(prose):
                fail(f"{markdown_file.name}:{line_number} uses label-shaped prose")


def validate_context_boundaries(skill_dir: Path) -> None:
    for markdown_file in markdown_files(skill_dir):
        for line_number, line in enumerate(markdown_file.read_text(encoding="utf-8").splitlines(), 1):
            if RESEARCH_CONTEXT_RE.search(line):
                fail(f"{markdown_file.name}:{line_number} contains research-only context")


def validate_links(skill_dir: Path) -> None:
    skill_file = skill_dir / "SKILL.md"
    skill_text = skill_file.read_text(encoding="utf-8")
    for reference in LINK_RE.findall(skill_text):
        if not (skill_dir / reference).is_file():
            fail(f"referenced file does not exist: {reference}")


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    required_files = (
        skill_dir / "README.md",
        skill_dir / "SKILL.md",
        skill_dir / "AGENTS.md",
        skill_dir / "LICENSE",
        skill_dir / "agents" / "openai.yaml",
    )
    for required_file in required_files:
        if not required_file.is_file():
            fail(f"{required_file.relative_to(skill_dir)} is missing")

    skill_file = skill_dir / "SKILL.md"
    ui_file = skill_dir / "agents" / "openai.yaml"
    skill_text = skill_file.read_text(encoding="utf-8")
    if not skill_text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    frontmatter_end = skill_text.find("\n---\n", 4)
    if frontmatter_end == -1:
        fail("SKILL.md frontmatter is not closed")

    frontmatter = skill_text[4:frontmatter_end]
    name_match = re.search(r"^name:\s*([^\s]+)\s*$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if name_match is None or name_match.group(1) != EXPECTED_NAME:
        fail(f"SKILL.md name must be {EXPECTED_NAME}")
    if description_match is None or not description_match.group(1).strip("'\""):
        fail("SKILL.md description must be non-empty")
    if PLACEHOLDER_RE.search(skill_text):
        fail("SKILL.md contains an unfinished placeholder")

    ui_text = ui_file.read_text(encoding="utf-8")
    if not re.search(r'^\s*display_name:\s*["\'].+["\']\s*$', ui_text, re.MULTILINE):
        fail("agents/openai.yaml needs a quoted display_name")
    if not re.search(r'^\s*short_description:\s*["\'].{25,64}["\']\s*$', ui_text, re.MULTILINE):
        fail("agents/openai.yaml needs a quoted 25-64 character short_description")

    validate_links(skill_dir)
    validate_markdown_fences(skill_dir)
    validate_prose_style(skill_dir)
    validate_context_boundaries(skill_dir)
    validate_workflows(skill_dir)
    validate_dependabot(skill_dir)

    print(f"Skill is valid: {EXPECTED_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
