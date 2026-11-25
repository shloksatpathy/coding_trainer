# C094 · Diagonals

The first line has `n` (1 ≤ n ≤ 100); then come `n` lines of `n` whole numbers. Print `main: S`, the sum of the diagonal from top-left to bottom-right, and `anti: T`, the sum of the diagonal from top-right to bottom-left.

**Example**

Input (also in `in.txt`):
```
3
1 2 3
4 5 6
7 8 9
```
Output:
```
main: 15
anti: 15
```

**Focus:** on the main diagonal the row equals the column; on the other one row + column = n - 1. One loop is enough.
