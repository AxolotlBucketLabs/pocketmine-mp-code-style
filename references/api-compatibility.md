# API compatibility

## Branch matrix

Read CONTRIBUTING.md before planning:

- Stable accepts bug fixes, API documentation improvements and base translation fixes. Style cleanup and code formatting changes are not accepted.
- Minor-next allows compatible improvements, selected non-disruptive features, deprecations and internal network changes under the documented limits.
- Major-next is the channel for removals and backwards-incompatible changes.
- Protocol changes are necessary internal changes and require the documented minor-release treatment.

The exact current branch and policy beat this summary.

## API boundary

Public and protected classes, functions and constants are API unless marked internal. Private members are generally not API except members introduced through traits. pocketmine/network/mcpe is implicitly internal as a whole. @deprecated is a compatibility bridge, not permission to delete a symbol.

## Before changing a public contract

Search:

- Repository call sites and tests.
- Named arguments and subclasses.
- Plugin-facing docs/examples.
- Serialization/config/world-data consumers.
- Deprecation/internal annotations.
- Branch and release policy.

Preserve parameter names when named arguments may be used. Avoid changing visibility, return/parameter types, exception order, event dispatch, serialized names or generated public registries without an explicit compatibility plan.

## Reporting

State whether the change is source-compatible, behavior-compatible, plugin-compatible, or deliberately breaking. A passing unit test does not establish compatibility with every plugin or client.
