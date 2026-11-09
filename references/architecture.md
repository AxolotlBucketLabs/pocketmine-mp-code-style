# Architecture and ownership

## Core lifecycle

PocketMine.php is the special startup file. Server owns the main lifecycle, plugin manager, network, worlds, schedulers, logger and shutdown coordination. The tick loop updates plugin schedulers, async completions, worlds, network and periodic maintenance. Put behavior in the owning subsystem instead of adding unrelated logic to the bootstrap.

## Plugins

PluginBase owns loader, server, description, data/resource paths, logger and scheduler. It calls onLoad during construction and exposes protected onEnable/onDisable hooks. Core-controlled enable state is final and internal. Commands declared in plugin metadata are registered by the base/manager path.

Before changing plugin behavior, inspect plugin metadata, PluginBase, PluginManager, a sibling plugin and tests. Keep a plugin entry point focused on lifecycle wiring when an existing subsystem owns the behavior.

## Events

Events are classes under pocketmine/event and normally dispatch with Event.call. Handler registration, inheritance order, cancellation and timing are framework behavior. Cancellable is implemented only when cancellation affects downstream handler dispatch. Use a sibling event as the template.

## Domain ownership

Blocks, items, entities, inventories, worlds, commands, permissions, network, scheduler and thread code each have established owners. Add behavior to the nearest owner and preserve its invariants. Do not introduce a catch-all utility or service to avoid learning the domain model.

## Network

pocketmine/network/mcpe is internal in its entirety and outside the API version system. It is valid core implementation code but not a stable plugin extension contract.
