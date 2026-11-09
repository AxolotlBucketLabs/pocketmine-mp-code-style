# Quality gates

## Required honesty

Before saying a change is complete, identify the command that proves each claim, run it, read its exit code and summary, and report the boundary. Never convert an unrun or partially run check into a pass.

## Gate selection

- Any PHP change: PHP-CS-Fixer dry-run and PHPStan as available.
- Behavior change: focused PHPUnit test.
- Plugin/server lifecycle or gameplay: integration and/or manual evidence.
- Generated input/codegen: composer update-codegen, clean diff and collision check.
- Translation resources: translation verifier.
- Shell scripts: ShellCheck.
- Dependency/PHP floor: Composer install/validate and the relevant PHP runtime/matrix.
- Public API: consumer search, API-focused tests and branch-policy review.

## Diff review

Inspect git diff and git diff --check. Look for unrelated formatting, accidental public API changes, changed serialized keys, generated files without inputs, dependency drift, missing tests and stale docs. Check status after every tool that can write files.

## Known snapshot caveat

The audited snapshot's local PHP was 8.4 while PHP-CS-Fixer 3.75's supported environment was PHP 8.3. A dry-run was possible only with the tool's environment guard overridden. Record this kind of caveat instead of hiding it.
