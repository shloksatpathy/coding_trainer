# P34 · Merge two sorted lists

Read `n`, a line of `n` sorted integers, `m`, and a line of `m` sorted integers (n, m ≥ 0, n + m ≥ 1; an empty list is an empty line). Merge them into one sorted list by relinking the existing nodes (no new nodes) and print it.

**Focus:** a dummy head node removes the special case for the first node. **Rust:** `fn merge(a: Option<Box<Node>>, b: Option<Box<Node>>) -> Option<Box<Node>>` written recursively is the easiest version.

**Sample input** (also in `in.txt`):
```
3
1 3 5
4
2 4 6 8
```
