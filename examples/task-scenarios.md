# Skill validation scenarios

Use these prompts in an isolated checkout. They are designed to test behavior, not merely match headings.

1. Create a typed class in an existing domain directory. Expected: inspect namespace/path siblings, use the header, strict types, tabs, attached braces and imports, and choose final/private only after checking consumers.
2. Add a public method to an established class. Expected: preserve parameter names and compatibility, use native types, add only useful PHPDoc, update a focused test, and search call sites.
3. Create an immutable value object. Expected: use final/private/readonly only when no subclassing, mutation or serialization contract forbids it.
4. Refactor a function with nested branches. Expected: keep the change minimal, preserve exception/event order, run focused tests and avoid a stable style sweep.
5. Add a class where final/private/readonly are tempting. Expected: search subclasses, reflection, lifecycle calls and public consumers before adding modifiers.
6. Add a custom exception. Expected: reuse the nearest domain hierarchy, document observable throws, keep American English and preserve caller handling.
7. Write a PHPUnit test. Expected: match local fixture/setup/assertion style and run the exact PHPUnit command.
8. Add an event or listener. Expected: follow Event.call, HandlerListManager, cancellation and inheritance semantics. Add ordering and cancellation coverage.
9. Change performance-sensitive code. Expected: classify main-thread, pooled CPU or dedicated thread work and preserve tick/cache/ownership invariants.
10. Change a public API. Expected: inspect branch matrix, call sites, named arguments, protected subclasses, deprecation and compatibility strategy.
11. Touch generated source. Expected: locate the generator/input, edit the source of truth, regenerate, check collision and clean diff.
12. Review a file with style violations. Expected: use finder scope and repository fixer/PHPStan evidence, not generic PHP style.
13. Find a legacy file that conflicts with the formatter. Expected: check exclusions, generator/mapper needs and branch. Preserve unrelated legacy code.
14. Edit a file outside formatter scope. Expected: do not impose core PHP-CS-Fixer rules. Inspect the owning tool/template convention.
15. Request PHP 8.4-only syntax. Expected: compare Composer floor/CI matrix and propose a PHP 8.1-compatible alternative or report an intentional compatibility change.
16. Ask for a convention with insufficient evidence. Expected: mark it unknown, inspect more siblings or ask a focused question. Never invent a MUST rule.
