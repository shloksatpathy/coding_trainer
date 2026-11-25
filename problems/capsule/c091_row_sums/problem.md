# C091 · Row sums

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` whole numbers. Print the grid back, row by row with the numbers separated by spaces, and end each row with ` | S`, where S is the sum of that row.

**Example**

Input (also in `in.txt`):
```
2 3
1 2 3
4 5 6
```
Output:
```
1 2 3 | 6
4 5 6 | 15
```

**Focus:** a grid is an array of rows; `g[i][j]` is row `i`, column `j`.
