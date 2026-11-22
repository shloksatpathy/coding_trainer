# P68 · Escape the maze

Read `r c`, then r rows: `S` start, `E` exit, `#` wall, `.` open. Moving up/down/left/right costs 1 step. Print the fewest steps from S to E, or `-1`.

**Focus:** BFS on the grid with a `dist` array initialised to -1. Find S while reading the grid.

**Sample input** (also in `in.txt`):
```
5 5
S.#..
..#.#
.##..
....#
#.#.E
```
