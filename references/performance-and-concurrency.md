# Performance and concurrency

## Classify the work

Choose the execution model before writing code:

- Main-thread/tick: world, entity, inventory, plugin lifecycle, event and network state that is not explicitly thread-safe.
- AsyncTask: brief CPU-bound work in the shared reusable pool, such as compression or world-generation calculations.
- Dedicated thread: work that runs for a long time or indefinitely.
- External worker/I/O: follow the existing subsystem. Do not move I/O into the shared AsyncPool by default.

## AsyncTask contract

AsyncTask.onRun cannot access Server and should not perform network, file or database I/O. Use onCompletion or other main-thread callbacks for server state. Store non-thread-safe values using the established local storage/serialization mechanisms. Keep tasks short. A pooled task that runs for seconds or longer harms other work.

## Tick and hot paths

Server and World have explicit tick invariants, queues and caches. Preserve ordering, timing instrumentation, cache invalidation and ownership. Use Event.hasHandlers in hot paths only when the local event pattern calls for it. Avoid allocations, logging, reflection and unbounded parsing in hot loops unless the existing subsystem does so intentionally.

## Verification

A static or unit test does not prove a frame/tick budget or real player load. For performance changes, run the focused test/reproducer, inspect timing/caching implications and report what was not measured. Do not call a successful PHPStan or PHPUnit run a performance result.
