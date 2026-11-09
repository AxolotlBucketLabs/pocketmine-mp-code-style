# Functions and control flow

Use this reference for method additions, refactors and bug fixes.

## Local patterns

- Prefer a guard clause when it makes an invalid state explicit and preserves the local flow.
- Use strict comparisons and explicit null handling in public/runtime code.
- Keep cleanup, timing and state restoration in finally blocks when the surrounding subsystem does so.
- Break long calls and expressions at semantic boundaries. Follow nearby continuation indentation.
- Keep short methods concise when the repository does. Do not expand or compress code for aesthetics alone.
- Avoid hidden dynamic construction, unsafe foreach mutation and unbounded parsing because project PHPStan rules reject those patterns.
- Use closures/arrow functions only when their capture, thread ownership and callable signature are clear.

## Refactor boundary

A stable bug fix should not become a control-flow or formatting sweep. Inspect callers and tests first, write the smallest behavior-preserving patch, then inspect the diff for unrelated changes. Performance-sensitive loops may favor an unusual but measured shape. Preserve that invariant and document intent if it is not obvious.

When a branch is deeply nested, refactor only if the task requires it or a focused test proves the behavior. Do not change exception order, event dispatch order, task ownership or serialization while claiming a style-only refactor.
