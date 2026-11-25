# C149 · Cheapest path

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` whole numbers ≥ 0, the cost of each cell. Walk from the top-left cell to the bottom-right one, moving only right or down. Print the smallest possible total cost of the cells you visit (both ends included).

**Example**

Input (also in `in.txt`):
```
3 3
1 3 1
1 5 1
4 2 1
```
Output:
```
7
```

**Focus:** dynamic programming on a grid: the cheapest way into a cell comes from the cheaper of the cell above and the cell to the left.
