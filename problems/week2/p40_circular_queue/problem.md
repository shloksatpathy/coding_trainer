# P40 · Circular queue

Implement a fixed-capacity queue with a ring buffer: an array of size `k`, a `head` index and a `count`. Read `k q`, then `q` commands:

- `enq x` — add x, or print `Full`
- `deq` — remove and print the front, or `Empty`
- `front` — print the front, or `Empty`
- `size` — print the count

**Focus:** the next slot is `(head + count) % k`; never shift elements. **Rust:** a struct with `buf: Vec<i64>`, `head: usize`, `count: usize` and `impl` methods returning `Option<i64>` / `bool`.

**Sample input** (also in `in.txt`):
```
2 7
enq 1
enq 2
enq 3
deq
enq 4
front
size
```
