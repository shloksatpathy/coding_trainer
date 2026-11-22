# P58 · BST insert and search

Read `n` and `n` integers; insert them into a binary search tree in that order (ignore duplicates). Then read `q` and `q` query values. Print the inorder traversal (sorted values), then `Found` or `Not found` for each query, one per line.

**Focus:** iterative insert and search — no recursion needed. Inorder of a BST is sorted; that's your self-check. **Rust:** `Option<Box<Node>>` with `while let Some(node) = cur` for search.

**Sample input** (also in `in.txt`):
```
7
50 30 70 20 40 60 80
3
60 25 20
```
