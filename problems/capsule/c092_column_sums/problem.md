# C092 · Column sums

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` whole numbers. Print the sum of each column, on one line, separated by spaces.

**Example**

Input (also in `in.txt`):
```
2 3
1 2 3
4 5 6
```
Output:
```
5 7 9
```

**Focus:** the loop order decides what you walk along: columns on the outside, rows on the inside.
