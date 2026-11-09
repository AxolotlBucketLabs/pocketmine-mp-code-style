---
name: pocketmine-mp-code-style
description: Use when creating, modifying, reviewing, or testing PHP in the Axolotl-PM PocketMine-MP repository. It preserves the repository's formatter, PHPStan, API-compatibility, lifecycle, generated-code, and branch-specific conventions.
---

# PocketMine-MP code style

Use the current PocketMine-MP checkout as the authority. This skill was derived from Axolotl-PM PocketMine-MP stable commit 7831952d6a970d1700ca82742ab2ac4dbe61ff80. Treat that revision as context only: re-check the current branch and nearby source before changing code.

## Operating rules

- Inspect the current branch, target file, nearby classes, callers, generated status, Composer constraints, and relevant tests before editing.
- Keep the smallest change that satisfies the task. Do not mix cleanup, formatter sweeps, dependency changes, or unrelated refactors into a focused change.
- Treat repository policy as higher priority than generic PHP standards. Do not apply PSR-12, Symfony, Laravel, or another formatter unless the repository actually requests it.
- Classify conclusions as configured/enforced, documented, observed, contextual, exception, conflicted, or unknown. Do not turn one source example into a universal rule.
- Never claim a check passed unless you ran it and read the exit status and summary.

## Branch and path gate

1. Read the branch before planning. On stable, style-only cleanup, code cleanup, API additions/removals, and breaking changes are restricted by CONTRIBUTING.md. A style-only stable request is a policy conflict, not permission to reformat.
2. Resolve whether the file is inside the PHP-CS-Fixer finder. The normal scope is src, generated, build, tests, and tools. PocketMine.php, JSON-mapper model directories, Bedrock upgrade model directories, and the optional DevTools path are excluded.
3. Classify generated, vendor, submodule, resource, and external-package files before editing. Generated output is not a handwritten source of truth.
4. Read the relevant reference below and then inspect a sibling implementation from the current checkout.

## Workflow

1. Understand whether the task is add, modify, fix, refactor, review, test, documentation, generated-code, or API work.
2. Inspect the branch, path, namespace, nearby types, public/protected consumers, lifecycle order, dependencies, tests, and generator inputs.
3. Load only the relevant references.
4. Plan the minimal compatible change. Preserve public/protected signatures, serialization formats, event ownership, tick/thread boundaries, and extension points unless the task explicitly targets a compatible branch and contract change.
5. Implement with the repository header, strict types, tabs, attached braces, ordered imports, native types and useful PHPDoc.
6. Validate with the strongest applicable checks: PHP-CS-Fixer dry-run, PHPStan, PHPUnit, codegen, translation/ShellCheck, integration or manual testing.
7. Inspect the final diff for unrelated whitespace, generated edits, accidental API changes, missing tests and unsupported PHP syntax.
8. Report changed files, rules applied, commands and results, skipped checks, environment limits and remaining risk.

## High-value rules

- Use the project header and declare(strict_types=1) in formatter-scope PHP.
- Use tabs and LF. Use short arrays, one-per-line ordered imports, explicit native function/constant imports in namespaces, and the repository's attached-brace style.
- Use native types compatible with PHP 8.1. Use PHPDoc for generics, array shapes, callable signatures, aliases, variance, throws, internal and deprecated contracts. Do not add redundant tags.
- Prefer final/private/readonly only after checking extension and lifecycle contracts. Do not make PluginBase, events, blocks, entities, inventories, worlds, or other mutable framework objects immutable by reflex.
- PHPStan level 9 and the six project rules are part of the contract. Avoid dynamic new, foreach by-reference, unsafe numeric-string keys, unbounded untrusted explode, forbidden enum comparisons, and deprecated legacy enum access.
- Keep plugin behavior in PluginBase/metadata and event behavior in the event handler contract. Use TaskScheduler for tick work. AsyncTask is for brief CPU-bound work. Its onRun method cannot access Server and should not do I/O.
- Treat pocketmine/network/mcpe as internal and outside API-version guarantees.
- Change generator inputs or codegen scripts, then regenerate. Never hand-edit generated output.
- Search consumers before changing public/protected symbols, visibility, named arguments, serialized data or exception behavior.

## Reference routing

Read only what the task needs:

- Repository/version, path scope, dependency floor: [repository-context.md](references/repository-context.md)
- Formatter, imports, braces, file exclusions: [formatting.md](references/formatting.md)
- Names and module placement: [naming.md](references/naming.md)
- Native types, PHPDoc and PHPStan: [php-types-and-phpdoc.md](references/php-types-and-phpdoc.md)
- Final/private/readonly and object boundaries: [class-design.md](references/class-design.md)
- Control flow and minimal refactors: [functions-and-control-flow.md](references/functions-and-control-flow.md)
- Plugin, event, world, block and item architecture: [architecture.md](references/architecture.md)
- Event/listener, plugin lifecycle and generated registry patterns: [pocketmine-patterns.md](references/pocketmine-patterns.md)
- Exceptions, legacy and conflicts: [error-handling.md](references/error-handling.md) and [exceptions.md](references/exceptions.md)
- AsyncTask, ticks, threads and performance: [performance-and-concurrency.md](references/performance-and-concurrency.md)
- Public API, branches and internal namespaces: [api-compatibility.md](references/api-compatibility.md)
- PHPUnit, integration and manual boundaries: [testing.md](references/testing.md)
- Exact quality commands and truthful reporting: [quality-gates.md](references/quality-gates.md)
- Fixed-commit evidence ledger: [evidence-index.md](references/evidence-index.md)
- Concrete examples and scenario tests: [examples/good-patterns.md](examples/good-patterns.md), [examples/anti-patterns.md](examples/anti-patterns.md), [examples/task-scenarios.md](examples/task-scenarios.md)

## Self-validation

Before reporting completion:

- Run the relevant repository checks and record exact output.
- Run the skill validator if the skill itself changed.
- Check all relative links in this skill.
- Inspect the diff or generated archive.
- Distinguish static analysis, unit tests, integration tests, manual testing, and production/client compatibility.
