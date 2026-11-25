# C053 · Right-aligned staircase

Read `n` ≥ 1. Print `n` lines: line `i` has `n - i` spaces and then `i` stars, so the stairs lean right.

**Example**

Input (also in `in.txt`):
```
4
```
Output:
```
   *
  **
 ***
****
```

**Focus:** two inner loops one after the other: first the padding, then the stars.
