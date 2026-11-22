# P32 · Reverse a linked list

Read `n` (n ≥ 1), then `n` integers. Build a linked list, reverse it **iteratively** by relinking `next` pointers (no new nodes, no array), and print it. Then reverse it back **recursively** and print it again.

**Focus:** the three-pointer loop `prev`, `cur`, `next`. **Rust:** with `Option<Box<Node>>` use `take()` to move nodes out: `while let Some(mut node) = cur { cur = node.next.take(); node.next = prev; prev = Some(node); }`.

**Sample input** (also in `in.txt`):
```
5
1 2 3 4 5
```
