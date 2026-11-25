# C080 · Checkpoint: moving average

The first line has `n` and `k` (1 ≤ k ≤ n ≤ 1000); the second has `n` whole numbers. For every run of `k` neighbouring numbers, from the left, print its average with 2 decimals, all on one line separated by spaces.

Keep a window sum: when the window moves one step, add the number that enters and subtract the one that leaves.

**Example**

Input (also in `in.txt`):
```
5 3
1 2 3 4 5
```
Output:
```
2.00 3.00 4.00
```

**Focus:** checkpoint for module 8: arrays, index arithmetic and updating a running value instead of recomputing it.
