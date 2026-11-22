# P81 · Maximum subarray (Kadane)

Read `n`, then `n` integers. Print the largest sum of a non-empty contiguous subarray.

Sample: `-2 1 -3 4 -1 2 1 -5 4` → `6` (`4 -1 2 1`)

**Analysis:** Kadane: `cur = max(x, cur + x)`, `best = max(best, cur)`. This is DP with O(1) memory. Make sure an all-negative array returns its largest element, not 0.

**Sample input** (also in `in.txt`):
```
9
-2 1 -3 4 -1 2 1 -5 4
```
