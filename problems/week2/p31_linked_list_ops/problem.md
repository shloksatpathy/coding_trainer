# P31 · Singly linked list

Implement a singly linked list with `head` and `tail` pointers. Read `q`, then `q` commands:

- `push_front x`, `push_back x`
- `pop_front`, `pop_back` — print the removed value, or `Empty`
- `print` — print the list, or `Empty`

**Focus:** C: `struct Node { int val; struct Node *next; }` with `malloc`/`free`. C++: same with `new`/`delete`. Python: a `Node` class. **Rust:** `Option<Box<Node>>` for `next` — `pop_back` needs a walk to the second-last node, and a tail pointer is hard in safe Rust; it's fine to drop it and walk.

**Sample input** (also in `in.txt`):
```
7
push_back 1
push_back 2
push_front 0
print
pop_back
pop_front
print
```
