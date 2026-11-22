# P60 · BST delete

Read `n` and `n` integers; insert them into a BST in order (ignore duplicates). Then read `m` and `m` keys; delete each key if present. When a node has two children, copy the value of its inorder successor (the minimum of its right subtree) into it, then delete that successor from the right subtree.

Print the preorder traversal of the final tree, or `Empty`.

**Focus:** three cases — leaf, one child, two children. **Rust:** `fn delete(node: Option<Box<Node>>, key: i64) -> Option<Box<Node>>` that takes ownership and returns the new subtree avoids most borrow fights.

**Sample input** (also in `in.txt`):
```
7
50 30 70 20 40 60 80
3
20 30 50
```
