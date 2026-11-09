# PocketMine-MP Code Style Skill

[![CI](https://github.com/AxolotlBucketLabs/pocketmine-mp-code-style/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/AxolotlBucketLabs/pocketmine-mp-code-style/actions/workflows/validate.yml) [![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Discord](https://img.shields.io/discord/1568295845374206052?label=discord&logo=discord&color=5865F2)](https://discord.gg/Pk4FrNvHnM)

PocketMine-MP Code Style is a repository-specific Codex skill for creating, modifying, reviewing, and testing PHP in Axolotl-PM PocketMine-MP.

The skill records the repository's formatter, PHPStan, API compatibility, lifecycle, generated-code, concurrency, testing, and branch conventions. It treats the current PocketMine-MP checkout as the source of truth and uses the audited commit only as a traceable baseline.

## Scope

- PocketMine-MP core source and repository tooling.
- PHP-CS-Fixer, PHPStan, PHPUnit, code generation, and collision checks.
- Plugin lifecycle, events, scheduler boundaries, world state, and internal network code.
- Public API compatibility, branch policy, generated output, and exception handling.
- Evidence-based style guidance with explicit exceptions and uncertainty labels.

This skill does not replace the target repository's current instructions. Re-check the branch, configuration, nearby implementation, consumers, and tests before applying a rule.

## Layout

```text
pocketmine-mp-code-style/
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       └── validate.yml
├── AGENTS.md
├── LICENSE
├── README.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   ├── anti-patterns.md
│   ├── good-patterns.md
│   └── task-scenarios.md
├── references/
│   └── ...
├── scripts/
│   └── validate_skill.py
└── tests/
    └── test_validate_skill.py
```

## Installation

Install this repository as a Codex skill using the Codex skill installer with `AxolotlBucketLabs/pocketmine-mp-code-style` as the GitHub source.

For a manual installation, place the repository folder at:

```text
~/.codex/skills/pocketmine-mp-code-style
```

Keep the folder name and the `name` value in `SKILL.md` aligned so automatic skill discovery can identify the skill consistently.

## Development

Run the repository validator after editing the skill:

```sh
python scripts/validate_skill.py
```

Run the validator regression tests:

```sh
python -m unittest discover --start-directory tests --pattern "test_*.py"
```

Run the official Codex skill validator before publishing a revision. Review every linked reference, example, workflow, and the final diff after the local checks pass.

## Audited baseline

The initial rules were derived from Axolotl-PM PocketMine-MP `stable` commit `7831952d6a970d1700ca82742ab2ac4dbe61ff80`.

That commit is evidence for the initial rule set, not a substitute for the current checkout. Refresh the evidence when the repository moves across branches, PHP versions, formatter configuration, API policy, or generated-code design.

## License

This project is released under the MIT License.
