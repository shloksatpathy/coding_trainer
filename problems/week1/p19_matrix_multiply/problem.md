# P19 · Matrix multiplication

Read `r1 c1` and r1 rows of matrix A, then `r2 c2` and r2 rows of matrix B. Print A × B one row per line (values separated by spaces), or `Invalid` if `c1 ≠ r2`.

Sample input:
```
2 2
1 2
3 4
2 2
5 6
7 8
```
Output:
```
19 22
43 50
```

**Analysis:** three nested loops give O(r1 · c1 · c2). In C, use a 2D array with fixed max size (100×100); in Rust, `vec![vec![0; c2]; r1]`.

**Sample input** (also in `in.txt`):
```
2 2
1 2
3 4
2 2
5 6
7 8
```
