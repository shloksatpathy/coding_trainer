# C073 · Find them all

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. The third line has a target `x`. Print `count: K`, how many times `x` appears, and `positions: …` with its positions (counting from 1) separated by spaces, or `positions: none`.

**Example**

Input (also in `in.txt`):
```
6
4 2 4 4 1 2
4
```
Output:
```
count: 3
positions: 1 3 4
```

**Focus:** a linear search: look at every element and remember the ones that match.
