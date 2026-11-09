# PHP types, PHPDoc and PHPStan

## Native types

The Composer floor is PHP 8.1. Use native parameter, return and property types for real contracts when that syntax is available: nullable, union, intersection, static, self, parent, iterable, callable, closures and class-string where appropriate. Preserve legacy public signatures when changing a stable API.

The codebase is strict-typed in the formatter scope. Do not use a newer PHP feature just because the local runtime supports it. Check Composer and the CI matrix first.

## PHPDoc

Use PHPDoc when it adds information PHP cannot express:

- Generic collections and variance.
- Array shapes and list/key types.
- Callable or closure signatures.
- PHPStan type aliases and imported aliases.
- Template parameters and inheritance.
- Deprecation, internal, compatibility and lifecycle notes.
- Observable throws contracts.
- Serialized or domain invariants.

Use native types instead of repeating them in PHPDoc. PHP-CS-Fixer enables no_superfluous_phpdoc_tags while allowing mixed where needed. Keep PHPDoc aligned and trimmed.

Examples from the source include World type aliases, TaskScheduler templates, RuntimeData generics and collection annotations.

## Project PHPStan rules

The configuration runs level 9, strict rules and PHPUnit extensions. It scans build, src, generated, PHPStan rules, PHPUnit, TesterPlugin and tools, with a bootstrap, stubs and dynamic constants.

The six custom rules are:

- DeprecatedLegacyEnumAccessRule: Do not add deprecated legacy enum access.
- DisallowDynamicNewRule: Do not instantiate using an expression such as `new $class(...)`. Use a typed closure or factory pattern.
- DisallowEnumComparisonRule: Use the enum/value API expected by the repository rather than direct forbidden comparisons.
- DisallowForeachByReferenceRule: Do not use foreach by-reference because of surprising mutation.
- ExplodeLimitRule: Pass a limit when untrusted input could create resource waste.
- UnsafeForeachRule: Make key types explicit. Avoid numeric-string coercion surprises and unspecified keys.

Read the implementation when a finding is involved. The config has counted ignores for platform/tool limitations. A passing analysis does not mean every design rule is static.

## Validation

Run:

~~~text
vendor/bin/phpstan analyze --no-progress --memory-limit=2G
~~~

Then run the narrowest PHPUnit test. Do not suppress or widen a finding merely to make the check pass without a repository-backed reason.
