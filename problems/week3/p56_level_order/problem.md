# P56 · Height and level order

Read a binary tree (non-empty). Print `height=H` (number of nodes on the longest root-to-leaf path), then the nodes level by level, one level per line, left to right.

The tree is given on one line in level order; `N` marks a missing child (LeetCode style). Example: `1 2 3 N 4` is 1 with children 2 and 3, and 2 has right child 4.

**Focus:** BFS with a queue; process the queue in batches of its current size to know where a level ends. **Rust:** `VecDeque`.

**Sample input** (also in `in.txt`):
```
3 9 20 N N 15 7
```
