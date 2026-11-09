# Testing

## Select the boundary

- PHPUnit proves isolated/domain behavior and is the default for logic that can be tested without a running server.
- PHPStan proves configured static contracts, not runtime lifecycle or client behavior.
- PHP-CS-Fixer proves configured formatting, not semantics.
- Codegen proves generated output is reproducible from inputs.
- Integration tests build DevTools/server artifacts and launch a server with test plugins.
- Manual playtesting is required when the behavior is gameplay/client-facing and cannot be adapted to PHPUnit.

## Repository commands

Use the current CI commands where available:

~~~text
vendor/bin/phpunit --bootstrap vendor/autoload.php --fail-on-warning tests/phpunit
vendor/bin/phpstan analyze --no-progress --memory-limit=2G
php-cs-fixer fix --dry-run --diff --ansi
composer update-codegen
php build/codegen/check-file-collisions.php
./tests/travis.sh -t4
~~~

The integration command requires initialized submodules and a compatible runtime. Do not run destructive or external release workflows merely to validate a source change.

## Test style

Match the nearest test class, fixture, setup/teardown and assertion vocabulary. Keep tests focused on observable behavior and lifecycle. Do not weaken assertions, delete tests or add mocks that bypass the behavior under test.

## Evidence reporting

Report exact test counts or command summaries when available. Separate passed, failed, skipped, unavailable and not-run. Do not imply that unit/static checks cover real-client, production or performance behavior.
