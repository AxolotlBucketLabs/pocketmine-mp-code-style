#!/usr/bin/env python3
"""Regression tests for the skill repository validator."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_skill.py"
SPEC = importlib.util.spec_from_file_location("validate_skill", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


VALID_SHA = "0123456789abcdef0123456789abcdef01234567"


class WorkflowPolicyTests(unittest.TestCase):
    def write_workflow(self, root: Path, uses_line: str) -> None:
        workflow_dir = root / ".github" / "workflows"
        workflow_dir.mkdir(parents=True)
        (workflow_dir / "validate.yml").write_text(
            f"name: Validate\nsteps:\n  - name: Check action\n    {uses_line}\n",
            encoding="utf-8",
        )

    def test_full_sha_with_version_comment_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_workflow(root, f"uses: actions/checkout@{VALID_SHA} # v7.0.1")
            VALIDATOR.validate_workflows(root)

    def test_mutable_action_ref_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_workflow(root, "uses: actions/checkout@main # v7.0.1")

            with self.assertRaisesRegex(SystemExit, "mutable action ref"):
                VALIDATOR.validate_workflows(root)

    def test_short_action_ref_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_workflow(root, "uses: actions/checkout@v7 # v7.0.1")

            with self.assertRaisesRegex(SystemExit, "full commit SHA"):
                VALIDATOR.validate_workflows(root)

    def test_missing_version_comment_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_workflow(root, f"uses: actions/checkout@{VALID_SHA}")

            with self.assertRaisesRegex(SystemExit, "version comment"):
                VALIDATOR.validate_workflows(root)


class DependabotPolicyTests(unittest.TestCase):
    def test_github_actions_update_configuration_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            github_dir = root / ".github"
            github_dir.mkdir()
            (github_dir / "dependabot.yml").write_text(
                "version: 2\nupdates:\n  - package-ecosystem: github-actions\n    directory: /\n",
                encoding="utf-8",
            )

            VALIDATOR.validate_dependabot(root)

    def test_missing_github_actions_update_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            github_dir = root / ".github"
            github_dir.mkdir()
            (github_dir / "dependabot.yml").write_text(
                "version: 2\nupdates: []\n",
                encoding="utf-8",
            )

            with self.assertRaisesRegex(SystemExit, "must update GitHub Actions"):
                VALIDATOR.validate_dependabot(root)


class MarkdownPolicyTests(unittest.TestCase):
    def write_prose_fixture(self, root: Path, text: str) -> None:
        (root / "README.md").write_text(text, encoding="utf-8")
        (root / "SKILL.md").write_text("# Example\n", encoding="utf-8")
        (root / "AGENTS.md").write_text("# Instructions\n", encoding="utf-8")
        (root / "references").mkdir()
        (root / "examples").mkdir()

    def test_balanced_fences_are_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_prose_fixture(root, "# Example\n\n```php\n$value = 1;\n```\n")
            VALIDATOR.validate_markdown_fences(root)

    def test_unclosed_fence_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_prose_fixture(root, "# Example\n\n```php\n")

            with self.assertRaisesRegex(SystemExit, "unclosed"):
                VALIDATOR.validate_markdown_fences(root)

    def test_valid_prose_ignores_code_and_inline_literals(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_prose_fixture(
                root,
                "# Example\n\n- Use `;` in the regular expression.\n\n```php\n$value = 1;\n```\n",
            )
            VALIDATOR.validate_prose_style(root)

    def test_semicolon_in_prose_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_prose_fixture(root, "# Example\n\nThis sentence has a semicolon; here.\n")

            with self.assertRaisesRegex(SystemExit, "forbidden prose punctuation"):
                VALIDATOR.validate_prose_style(root)

    def test_lowercase_bullet_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_prose_fixture(root, "# Example\n\n- start with lowercase.\n")

            with self.assertRaisesRegex(SystemExit, "lowercase prose"):
                VALIDATOR.validate_prose_style(root)

    def test_research_context_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.write_prose_fixture(root, "# Example\n\nPoggit is research context only.\n")

            with self.assertRaisesRegex(SystemExit, "research-only context"):
                VALIDATOR.validate_context_boundaries(root)


if __name__ == "__main__":
    unittest.main()
