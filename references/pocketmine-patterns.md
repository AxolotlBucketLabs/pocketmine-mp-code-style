# PocketMine patterns

## Events and listeners

Read Event.php, Cancellable.php, HandlerListManager and a related event before adding an event. Preserve:

- The event base class and namespace.
- Payload ownership and mutability.
- Handler registration and inheritance behavior.
- Cancellable semantics and handleCancelled behavior.
- Event.call timing and recursion protection.
- Tests for ordering and cancellation where relevant.

Do not invoke listeners directly or add cancellation merely because a name sounds cancellable.

## Plugins

Use PluginBase lifecycle hooks and metadata. Core calls onLoad, onEnable and onDisable through PluginBase. Core-owned state-changing methods are not plugin extension points. Use the plugin scheduler and manager APIs rather than reaching into internal server arrays.

## Scheduler

TaskScheduler queues Task handlers and runs them from mainThreadHeartbeat. For a repeating or delayed task, use the existing scheduling methods and cancellation semantics. Match task naming and test patterns in tests/phpunit/scheduler.

## Blocks, items and registries

Blocks/items use domain base classes, interfaces and registry/input classes. Generated Vanilla* registries point to source input classes. When adding vanilla content, identify the registry input and the data/codegen pipeline first. Preserve clone/value semantics and local constructor patterns.

## Generated translations and Bedrock data

Known translation classes and Bedrock name/state files are generated. Change the input data or generator and run composer update-codegen. Do not hand-edit generated output.
