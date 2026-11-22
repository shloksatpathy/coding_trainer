# P46 · Three sum

Read `n`, then `n` integers. Print every distinct triplet `a b c` with a ≤ b ≤ c and a + b + c = 0, one per line in lexicographic order, or `None`.

Sample: `-1 0 1 2 -1 -4` → `-1 -1 2` / `-1 0 1`

**Analysis:** sort, fix the first element, then two pointers for the other two: O(n²) instead of O(n³). Skip equal neighbours to avoid duplicate triplets.

**Sample input** (also in `in.txt`):
```
6
-1 0 1 2 -1 -4
```
