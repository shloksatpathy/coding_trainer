# P79 · 0/1 knapsack

Read `n W`, then n lines `weight value`. Each item can be taken at most once. Print the maximum total value with total weight ≤ W.

**Analysis:** 1-D DP over capacity, iterating capacity **downwards** for each item so it isn't reused. O(n · W). Iterating upwards solves the unlimited version instead — try it.

**Sample input** (also in `in.txt`):
```
4 7
1 1
3 4
4 5
5 7
```
