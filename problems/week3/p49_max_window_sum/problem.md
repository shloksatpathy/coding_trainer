# P49 · Maximum sum window

Read `n k` (1 ≤ k ≤ n), then `n` integers. Print the maximum sum of `k` consecutive elements.

**Analysis:** keep the window sum and slide it: add the new element, subtract the one leaving. O(n) instead of O(n·k). The large test needs 64-bit sums.

**Sample input** (also in `in.txt`):
```
8 3
2 1 5 1 3 2 9 1
```
