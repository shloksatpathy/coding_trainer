# P66 · Count islands

Read `r c`, then r rows of c characters: `#` is land, `.` is water. Count the islands (groups of land connected up/down/left/right).

**Focus:** a grid is a graph — each cell is a vertex. Flood fill each new `#` with BFS or DFS and mark it visited. Use `dr = {-1, 1, 0, 0}`, `dc = {0, 0, -1, 1}` direction arrays.

**Sample input** (also in `in.txt`):
```
4 5
##..#
#...#
..#..
.....
```
