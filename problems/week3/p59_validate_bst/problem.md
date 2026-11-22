# P59 · Validate a BST

Read a binary tree (non-empty). Print `Valid` if it is a strict binary search tree — every value in a node's left subtree is smaller and every value in its right subtree is larger — else `Invalid`.

Samples: `2 1 3` → `Valid` · `5 1 4 N N 3 6` → `Invalid` · `5 4 6 N N 3 7` → `Invalid` (3 sits in 5's right subtree)

The tree is given on one line in level order; `N` marks a missing child (LeetCode style). Example: `1 2 3 N 4` is 1 with children 2 and 3, and 2 has right child 4.

**Focus:** checking only parent vs child is the classic bug (third sample). Pass down `(low, high)` bounds, or check that inorder is strictly increasing.

**Sample input** (also in `in.txt`):
```
2 1 3
```
