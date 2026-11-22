# P54 · N-Queens

Read `n` (1 ≤ n ≤ 10). Count the ways to place n queens on an n×n board so that no two attack each other. Print the count, then the lexicographically first solution as the 1-based column of the queen in each row, or `None`.

Sample `4` → `2` / `2 4 1 3`

**Focus:** place one queen per row; track used columns and both diagonals (`r + c` and `r - c + n - 1`) in boolean arrays so each check is O(1).

**Sample input** (also in `in.txt`):
```
4
```
