# P55 · Tree traversals

Read a binary tree (non-empty). Print its preorder, inorder and postorder traversals, one per line.

The tree is given on one line in level order; `N` marks a missing child (LeetCode style). Example: `1 2 3 N 4` is 1 with children 2 and 3, and 2 has right child 4.

**Focus:** build the tree with a queue while parsing. Recursive traversals are three lines each — then write inorder iteratively with an explicit stack. **Rust:** `Option<Box<Node>>` children work here; `Rc<RefCell<Node>>` is what LeetCode uses — try both.

**Sample input** (also in `in.txt`):
```
1 2 3 4 5 N 6
```
