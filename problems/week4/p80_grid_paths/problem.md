# P80 · Paths through a grid

Read `r c`, then r rows of `.` (open) and `#` (blocked). Moving only right or down, count the paths from the top-left to the bottom-right cell. Print the count modulo 1,000,000,007 (0 if a corner is blocked).

**Focus:** `paths[i][j] = paths[i-1][j] + paths[i][j-1]` for open cells, taken mod after each addition.

**Sample input** (also in `in.txt`):
```
3 3
...
.#.
...
```
