# C132 · Unique values

The first line has `n` (1 ≤ n ≤ 1000); the second has `n` whole numbers. Print the different values in the order they first appear, on one line, then `distinct: K`.

**Example**

Input (also in `in.txt`):
```
7
3 1 3 2 1 3 5
```
Output:
```
3 1 2 5
distinct: 4
```

**Focus:** a set remembers which values have been seen; asking "seen before?" is one step.
