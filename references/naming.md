# Naming and module placement

Use this reference when adding a class, method, property, event, task, registry or file.

## Path and namespace

Composer maps pocketmine to src and generated. Use the directory that owns the domain and the matching namespace. Typical domains include block, command, crafting, data, entity, event, inventory, item, network, permission, player, plugin, promise, resourcepacks, scheduler, thread, timings, utils and world.

Files use PascalCase.php for class-like types. Domain subdirectories mirror namespace segments. src/PocketMine.php is a special bootstrap exception.

## General observed names

These are strong conventions, not all absolute policy:

- Classes, interfaces, traits and enums: PascalCase.
- Methods, functions, properties and local variables: lowerCamelCase.
- Constants: UPPER_SNAKE_CASE.
- Tests: domain name plus Test where that is the local pattern.
- Exceptions: domain or failure name plus Exception.
- Events: domain plus Event.
- Tasks: operation plus Task.
- Managers/handlers/registries/parsers/serializers: use the suffix only when the class actually owns that responsibility.
- Boolean methods commonly use is, has, can, or should. Match the local API vocabulary.
- Get/set/create/from/to/load/save/read/write names must describe the real direction and ownership. Do not rename solely to match a generic verb list.

## Naming workflow

1. Search for the closest sibling type and its callers.
2. Confirm whether the new symbol is public, protected, internal or private.
3. Check collision and abbreviation conventions in that module.
4. Prefer domain terminology already present in API and tests.
5. Do not infer a required suffix from one class. Mark uncertain naming as observed until repeated evidence exists.

Generated and serialized names follow their generator/external schema. Do not rename generated constants or external fields for aesthetic consistency.
