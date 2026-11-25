# C049 · Smallest and largest

The first line has a whole number `n` ≥ 1; the second line has `n` whole numbers. Print `min: A` and `max: B`. Don't store the numbers: keep only the smallest and largest seen so far.

**Example**

Input (also in `in.txt`):
```
4
3 -1 7 2
```
Output:
```
min: -1
max: 7
```

**Focus:** tracking the best values while reading; start from the first value, not from 0.
