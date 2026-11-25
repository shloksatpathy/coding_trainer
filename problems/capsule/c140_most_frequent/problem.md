# C140 · Checkpoint: most frequent

The first line has `n` (1 ≤ n ≤ 200 000); the second has `n` whole numbers (|x| ≤ 10^9). Print `value: V` and `count: C` for the most frequent value (the smallest one if several tie), and `distinct: D`, the number of different values.

**Example**

Input (also in `in.txt`):
```
7
3 1 3 2 1 3 5
```
Output:
```
value: 3
count: 3
distinct: 4
```

**Focus:** checkpoint for module 14: counting with a map in one pass (or sorting and counting runs), fast enough for the large test.
