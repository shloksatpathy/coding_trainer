# C121 · First position

The first line has `n`; the second line has `n` whole numbers. (1 ≤ n ≤ 1000). Then comes `q` and a line of `q` values. For each value print the position (counting from 1) of its first occurrence, or `-1` if it isn't there, one per line.

**Example**

Input (also in `in.txt`):
```
5
4 2 4 9 1
4
4 9 7 1
```
Output:
```
1
4
-1
5
```

**Focus:** linear search: check the elements one by one and stop at the first match.
