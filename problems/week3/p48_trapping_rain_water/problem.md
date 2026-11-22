# P48 · Trapping rain water

Read `n`, then `n` non-negative bar heights. Print how many units of rain water are trapped between the bars.

Sample: `0 1 0 2 1 0 1 3 2 1 2 1` → `6`

**Analysis:** water above bar i = `min(maxLeft, maxRight) - h[i]`. Two pointers with running maxima do it in O(n) time and O(1) memory.

**Sample input** (also in `in.txt`):
```
12
0 1 0 2 1 0 1 3 2 1 2 1
```
