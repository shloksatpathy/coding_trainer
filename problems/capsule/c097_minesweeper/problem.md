# C097 · Minesweeper

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` characters each, with no spaces. Each character is `*` (a mine) or `.`. Print the grid with every `.` replaced by the number of mines among its up to 8 neighbours (also diagonally); mines stay `*`.

**Example**

Input (also in `in.txt`):
```
3 4
*...
..*.
....
```
Output:
```
*211
12*1
0111
```

**Focus:** visiting the neighbours of a cell, and checking the edges so you never look outside the grid.
