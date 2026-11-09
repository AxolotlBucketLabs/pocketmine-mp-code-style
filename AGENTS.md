# Repository instructions

These instructions apply only to the `pocketmine-mp-code-style` repository. Read them together with `SKILL.md` when maintaining this skill. They do not replace system instructions, user instructions, or the instructions of a target PocketMine-MP checkout.

## Keep the skill self-consistent

- Treat `SKILL.md` as the entrypoint and references as routed supporting guidance.
- Keep one canonical rule in one place. Link to it instead of copying a second version into another reference.
- Keep examples, scenarios, validator behavior, README structure, and repository instructions consistent.
- Treat the current PocketMine-MP checkout as authoritative when it differs from the audited baseline.
- Do not turn one source example or a historical audit result into a universal rule without current evidence.

## Repository-specific scope

- Preserve PocketMine-MP terminology and API names.
- Do not replace repository-specific rules with generic PSR-12, Symfony, Laravel, or another formatter without evidence from the target checkout.
- Keep branch policy, generated-code boundaries, internal namespaces, and compatibility exceptions visible in the routed references.
- Do not copy AxolotlBucketLabs permissions, roles, bypass rules, or private organization procedures into the technical skill.

## Prose and Markdown

- Write standalone bullet items as complete sentences that begin with an uppercase letter and end with a period.
- Avoid semicolons in ordinary prose. Use a period, comma, or a new sentence instead.
- Do not use em dash or en dash characters as sentence punctuation. Use an ASCII hyphen only when a dash is necessary.
- Use straight double quotes in authored prose.
- Keep code, regex, URLs, legal text, direct quotations, and literal syntax unchanged when the exception is required.
- Use inline code for literal technical terms and fenced code blocks for multiline code, configuration, commands, logs, patches, and output.

## Required checks

- Run `python scripts/validate_skill.py` after editing the skill.
- Run `python -m unittest discover --start-directory tests --pattern "test_*.py"` after changing validator behavior or its tests.
- Run the official Codex skill validator before publishing a revision.
- Review all human-facing Markdown files after a policy change.
- Report local checks, hosted CI, published releases, and external repository settings as separate evidence.
