# C096 · Count the walls

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` characters each, with no spaces. Each character is `#` (a wall) or `.` (floor). Print the number of walls in each row, one per line, then `total: T`.

**Example**

Input (also in `in.txt`):
```
3 4
#..#
....
####
```
Output:
```
2
0
4
total: 6
```

**Focus:** a grid of characters: each row is a piece of text, and `g[i][j]` is a character.
