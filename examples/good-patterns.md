# Good patterns

These are concise synthetic examples shaped by the audited source. They are SYNTHETIC EXAMPLES, not copied repository code.

## In-scope class

~~~php
<?php

/*
 * PocketMine project header goes here.
 */

declare(strict_types=1);

namespace pocketmine\example;

use pocketmine\utils\Utils;
use function count;

final class ExampleRegistry{
	private array $entries = [];

	public function add(string $name, object $entry) : void{
		$this->entries[$name] = $entry;
	}

	public function has(string $name) : bool{
		return isset($this->entries[$name]);
	}

	/**
	 * @return list<object>
	 */
	public function getAll() : array{
		return array_values($this->entries);
	}
}
~~~

Why it fits: strict types, attached braces, tabs, native types, one-per-line imports, useful PHPDoc and private owned state. Before using it, confirm the real target namespace and nearby class contract.

## Async boundary

~~~php
final class HashTask extends AsyncTask{
	public function __construct(
		private string $payload
	){
	}

	public function onRun() : void{
		$this->setResult(hash("sha256", $this->payload));
	}

	public function onCompletion() : void{
		// Main-thread code may consume the result here.
	}
}
~~~

This remains a synthetic pattern. Check the actual AsyncTask API and do not use it for I/O or long-running work.

## Event boundary

A new event should extend the current event family, expose typed payloads, implement Cancellable only when downstream handlers can suppress the operation, and use Event.call from the owner. Copy a sibling event and add ordering/cancellation tests rather than inventing a listener invocation mechanism.

## Generated boundary

Change VanillaBlocksInputs or the correct data/generator input, run composer update-codegen, run the collision check and inspect the generated diff. Do not patch generated/VanillaBlocks.php directly.
