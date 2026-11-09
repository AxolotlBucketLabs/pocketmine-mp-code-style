# Exceptions, conflicts and scope boundaries

## Conflict resolution

When sources disagree:

1. Identify the branch and commit.
2. Prefer current executable configuration/CI for the rule it actually enforces.
3. Read maintainer policy and current source.
4. Check whether the difference is intentional scope, generated code, external code, legacy, or accidental.
5. Preserve the narrower safe behavior and record unresolved conflict.

Do not choose a generic PHP convention merely because it is familiar.

## Known snapshot conflicts

- Composer permits PHP 8.1 and CI tests 8.1, while BUILDING.md says PHP 8.2 or newer. Use the declared Composer/CI syntax floor and disclose the build-doc discrepancy.
- Formatter scope excludes the bootstrap and mapper/model paths. Do not format them as ordinary core classes.
- CONTRIBUTING prefers final/private/readonly, while framework extension points and runtime state remain mutable.
- PHPStan level 9 has counted ignores for known tool/platform limitations. A clean run is not proof that all design constraints are static.
- Integration needs an initialized DevTools submodule. Not running it is a limitation, not a pass.

## Unknowns

If the current evidence cannot answer a naming, lifecycle or architecture question, mark it unknown, inspect more local evidence or ask a focused question. Do not create a MUST rule from a single file or upstream memory.
