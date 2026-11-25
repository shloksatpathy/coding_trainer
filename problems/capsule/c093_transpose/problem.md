# C093 · Transpose

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` whole numbers. Print the transposed grid: `c` lines of `r` numbers, where row `j` of the output is column `j` of the input.

**Example**

Input (also in `in.txt`):
```
2 3
1 2 3
4 5 6
```
Output:
```
1 4
2 5
3 6
```

**Focus:** swapping the roles of rows and columns: output `[j][i]` is input `[i][j]`.
