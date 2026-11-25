# C051 · Rectangle of #

Read a width `w` and a height `h` (both ≥ 1). Print a rectangle of `#`: `h` lines of `w` characters. Print one `#` at a time, with a loop inside a loop.

**Example**

Input (also in `in.txt`):
```
4 3
```
Output:
```
####
####
####
```

**Focus:** nested loops: the inner loop runs completely for every round of the outer one. Outer loop = rows, inner loop = columns.
