# P51 · Shortest subarray with sum ≥ s

Read `n s`, then `n` positive integers. Print the length of the shortest contiguous subarray whose sum is ≥ s, or `0` if there is none.

Sample: `n=6 s=7`, `2 3 1 2 4 3` → `2` (the subarray `4 3`)

**Analysis:** grow the window on the right, shrink from the left while the sum is still ≥ s. Each index enters and leaves once — O(n).

**Sample input** (also in `in.txt`):
```
6 7
2 3 1 2 4 3
```
