# Error handling

## Choose the existing contract

Before adding an exception:

1. Search the nearest domain exception hierarchy.
2. Inspect callers and tests for expected exception class/message/order.
3. Decide whether the condition is invalid user/client data, an impossible internal assumption, lifecycle misuse, or an I/O/data-load failure.
4. Preserve the existing translation/logging boundary.
5. Add a throws doc when the exception is an observable method contract.

Use the repository's domain exception when one exists. RuntimeException, LogicException and AssumptionFailedError are used for distinct contract/internal cases. Do not replace them with a generic Exception for convenience.

## Untrusted input

Validate and bound external/client/config data. The custom ExplodeLimitRule exists because unbounded splitting of malicious data can waste resources. Follow existing parsers and serializers rather than adding ad hoc string handling.

## Error messages

Write concise American English messages with actionable context. Preserve technical identifiers, translation keys and exception class names. Do not expose internal paths or secrets merely to make a message more verbose.

## Thread and lifecycle errors

Respect the thread boundary and lifecycle owner. A thread crash, async-task failure, event recursion, disabled scheduler or unloaded world has an established owner and error path. Read that path before adding a catch or retry. Never catch broadly just to make PHPStan quiet.
