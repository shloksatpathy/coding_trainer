# P15 · Binary search

Read `n`, then `n` sorted distinct integers, then a target. Print the target's index (0-based), or `-1` if it is missing. Write the loop yourself.

Sample: `1 3 5 7 9 11` target `7` → `3` · target `4` → `-1`

**Analysis:** compute `mid = lo + (hi - lo) / 2`, not `(lo + hi) / 2`, because the sum can overflow. Afterwards compare with the library versions: `bsearch`, `std::lower_bound`, `bisect`, `slice::binary_search`.

**Sample input** (also in `in.txt`):
```
6
1 3 5 7 9 11
7
```
