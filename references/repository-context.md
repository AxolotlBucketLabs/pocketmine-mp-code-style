# Repository context

This reference captures the audited Axolotl-PM PocketMine-MP stable snapshot. Re-check the current checkout before relying on a fact.

## Snapshot

- URL: https://github.com/axolotl-pm/PocketMine-MP
- Audited branch: stable
- Audited commit: 7831952d6a970d1700ca82742ab2ac4dbe61ff80
- Version constants: 5.51.2, development build, stable channel
- Fork relationship: the README identifies the repository as a fork of pmmp/PocketMine-MP
- Composer PHP requirement: ^8.1
- Composer platform PHP: 8.1.0
- CI matrix: PHP 8.1 through 8.5
- Required nonstandard extensions include chunkutils2, crypto, encoding, igbinary, leveldb, morton, pmmpthread and yaml
- Composer maps pocketmine to src and generated. Development mappings cover tests/phpunit and tests/phpstan/rules.

Primary sources:

- The `composer.json` file, lines 7-104.
- The `composer.lock` file at the audited commit.
- The `src/VersionInfo.php` file, lines 22-37.
- The `CONTRIBUTING.md` file, lines 44-75.
- The `BUILDING.md` file, lines 1-33.
- The `src/PocketMine.php` file, lines 58-173.

## Directory ownership

- The `src` directory contains handwritten core server source and APIs.
- The `generated` directory contains code generated from inputs and data.
- The `build` directory contains build and code-generation programs.
- The `tests/phpunit` directory contains domain and unit tests.
- The `tests/phpstan` directory contains PHPStan rules, config, stubs, and test-only types.
- The `tests/plugins` directory contains integration fixtures and the optional DevTools submodule.
- The `tools` directory contains standalone maintenance utilities.
- The `resources` directory contains runtime data, config, and translations.
- The `.github/workflows` directory contains CI, release, and maintenance automation.
- The `.idea` directory contains PhpStorm code style and file templates.
- The `vendor` directory contains external Composer code. Do not infer core style from it.

## Reconnaissance sequence

Before a change:

1. Run git status and identify the branch.
2. Read composer.json and composer.lock if a dependency or PHP syntax is involved.
3. Find the target path with git ls-files and compare it with .php-cs-fixer.php.
4. Search for sibling classes, call sites, subclasses, interfaces and tests.
5. If generated, locate the input and generator before opening the output.
6. If a branch or API question is involved, read CONTRIBUTING.md and the nearest API/internal README.
