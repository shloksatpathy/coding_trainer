# C095 · Largest cell

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` whole numbers. Print `max: V at R C`: the largest value and its row and column, counting from 1. If it appears more than once, give the first one in reading order (row by row, left to right).

**Example**

Input (also in `in.txt`):
```
2 3
1 9 3
9 5 6
```
Output:
```
max: 9 at 1 2
```

**Focus:** searching a grid while remembering where the best value was.
