# P76 · Longest increasing subsequence

Read `n`, then `n` integers. Print the length of the longest strictly increasing subsequence.

Sample: `10 9 2 5 3 7 101 18` → `4` (e.g. `2 3 7 18`)

**Analysis:** the O(n²) DP (`lis[i] = 1 + max lis[j] for j < i, a[j] < a[i]`) is fine up to a few thousand. The 100,000-number test needs O(n log n): keep `tails[len]` = smallest tail of an increasing subsequence of that length and binary search it (`lower_bound`, `bisect_left`, `partition_point`).

**Sample input** (also in `in.txt`):
```
8
10 9 2 5 3 7 101 18
```
