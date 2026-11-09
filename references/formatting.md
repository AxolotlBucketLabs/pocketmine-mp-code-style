# Formatting

Use this reference for PHP formatting or a style review.

## File shape

For files inside the PHP-CS-Fixer finder, use:

1. opening PHP tag
2. PocketMine ASCII/LGPL header
3. declare(strict_types=1)
4. namespace
5. imports
6. declarations

Use LF endings, a final newline, no closing PHP tag and no trailing whitespace. The fixer uses a blank line after the opening tag and after namespace, and a blank line before declare as configured. The exact finder is in .php-cs-fixer.php lines 3-16.

The repository excludes src/PocketMine.php, crafting/json, inventory/json, Bedrock upgrade model directories and the optional DevTools path. Do not run a whole-repository formatter as if those files had the same contract.

## Indentation and braces

- PHP uses tabs. The configured tab size is four spaces for editor display.
- YAML uses two spaces.
- PhpStorm confirms no space before control parentheses and no space before opening braces.
- Source shape is class Server{, function run(){ and if(condition){.
- Use one space after casts and one space before the return-type colon.
- Preserve semantic indentation for arrays, multiline calls, closures and chained expressions. Do not hand-align unrelated code.

## Arrays and operators

- Use short array syntax.
- Use the configured single-space binary operator and concat style.
- Use the configured unary and cast spacing.
- Keep configured blank-line rules. Do not add decorative blank lines.
- Use a trailing comma in a multiline list when nearby code and the parser version support it.

## Imports

- One import per statement.
- Ordered imports are grouped class, function, const and alpha-sorted within the configured groups.
- In namespaced files, native functions and constants are normally imported explicitly. Source examples include use function count and use const PHP_INT_MAX.
- Keep aliases when they prevent collisions or clarify a generated registry/input. Do not shorten fully qualified names in excluded JSON-mapper doc comments.
- Remove unused imports.

## PhpStorm and fixer

The project style is in .idea/codeStyles/Project.xml. The complete PHP-CS-Fixer rule list is in the audited source configuration. CI invokes PHP-CS-Fixer in dry-run/diff mode. Use the tool as the final formatting authority for in-scope files. Do not run it in write mode across unrelated files.

## Safe review checklist

- Is the target path in finder scope?
- Is the file generated or a mapper exception?
- Is strict_types present where expected?
- Are tabs and LF preserved?
- Are imports sorted and complete?
- Are braces/parentheses/return types shaped like siblings?
- Did formatting change unrelated lines?
