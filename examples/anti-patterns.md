# Anti-patterns

These are SYNTHETIC EXAMPLES. They describe behavior rejected by the audited repository or unsafe agent behavior. They are not claims that the exact snippets occur in source.

## Generic formatter override

~~~php
class Example {
    public function run() {
        $values = array(1, 2);
    }
}
~~~

Why it is wrong for normal formatter-scope code: it uses spaces, a space before the brace, untyped members/methods and long array syntax. Use the repository fixer and nearby source.

## Dynamic construction and foreach reference

~~~php
$object = new $className($argument);
foreach($items as &$item){
	$item = normalize($item);
}
~~~

Why it is wrong: project PHPStan rules reject dynamic new and foreach by-reference. Use a typed closure/factory or a deliberate copy/update pattern.

## Unsafe untrusted parsing

~~~php
$parts = explode(",", $clientData);
~~~

Why it is wrong: pass a limit when untrusted input can create unbounded work. Read the ExplodeLimitRule and existing parser.

## Async misuse

~~~php
final class BadTask extends AsyncTask{
	public function onRun() : void{
		$this->server->getLogger()->info("running");
		file_get_contents($this->url);
		while(true){
			$this->poll();
		}
	}
}
~~~

Why it is wrong: AsyncTask onRun cannot use Server, should not do I/O and should be short-lived. Classify the work first.

## Generated edit

Editing generated/VanillaBlocks.php by hand is not a complete change. Find VanillaBlocksInputs.php or the data/codegen source, regenerate, and check for a clean reproducible diff.

## Stable cleanup

A request to reformat every file on stable conflicts with CONTRIBUTING.md. Report the branch-policy conflict instead of creating a broad formatting diff.
