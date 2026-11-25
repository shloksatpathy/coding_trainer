# C129 · Closest values

The first line has `n`; the second line has `n` whole numbers. (2 ≤ n ≤ 200 000). Print the smallest difference between any two of them (at different positions).

**Example**

Input (also in `in.txt`):
```
5
10 3 17 8 1
```
Output:
```
2
```

**Focus:** sorting first turns a question about all pairs into a question about neighbours: the closest two values are next to each other once sorted.
