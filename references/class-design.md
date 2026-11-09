# Class design

## Decision sequence

Before adding or changing a class:

1. Determine whether the class is an extension point, data/value object, lifecycle manager, generated binding, or test fixture.
2. Search subclasses, implementers, reflection, named-argument callers and public consumers.
3. Check whether state is constructor-owned, mutable by tick/lifecycle, shared across threads, or serialized.
4. Choose the narrowest visibility and smallest abstraction that preserves those contracts.
5. Add final/private/readonly only when the change does not remove a supported extension or mutation behavior.

## Repository evidence

CONTRIBUTING.md says to use final, private and readonly wherever possible and to avoid unnecessary setters/public writable properties. This is a preference with real exceptions:

- PluginBase, events, blocks, entities and commands commonly need subclassing.
- Server, World, inventories and entity state intentionally mutate.
- Generated registries and utility/value-like classes are often final.
- Core-controlled lifecycle methods can be final even when the class is abstract.
- Public writable properties may be data-transfer or runtime-timing contracts.

Constructor promotion is common for stable dependencies. Private fields are preferred for owned state. Protected state is retained where subclasses are part of the design.

Do not introduce a DI container, singleton, repository pattern, immutable wrapper or new framework solely to make a class look cleaner. Fit the owner and nearby abstractions.
