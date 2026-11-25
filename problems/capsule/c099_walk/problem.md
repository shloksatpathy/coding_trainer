# C099 · A walk on the grid

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` characters each, with no spaces. `#` is a wall and `.` is floor; the top-left cell is always floor. The last line is a word of moves: `U`, `D`, `L`, `R` (up, down, left, right). Start at the top-left cell and follow the moves, skipping any move that would go into a wall or off the grid. Print `at R C` (counting from 1) and `moved: K`, the number of moves actually made.

**Example**

Input (also in `in.txt`):
```
3 4
..#.
.#..
....
DDRRRUUR
```
Output:
```
at 1 4
moved: 7
```

**Focus:** a simulation: a position that changes step by step, with each step checked before it is taken.
