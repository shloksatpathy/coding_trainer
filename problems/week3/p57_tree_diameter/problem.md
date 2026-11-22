# P57 · Tree diameter

Read a binary tree (non-empty). Print its diameter: the number of edges on the longest path between any two nodes (the path need not pass through the root).

Sample: `1 2 3 4 5` → `3` (4 → 2 → 1 → 3)

The tree is given on one line in level order; `N` marks a missing child (LeetCode style). Example: `1 2 3 N 4` is 1 with children 2 and 3, and 2 has right child 4.

**Analysis:** one post-order pass that returns each subtree's height and updates `best = max(best, hl + hr)` — O(n), not O(n²).

**Sample input** (also in `in.txt`):
```
1 2 3 4 5
```
