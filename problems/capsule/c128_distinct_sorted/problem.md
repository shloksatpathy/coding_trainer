# C128 · Distinct values

The first line has `n` (1 ≤ n ≤ 1000); the second has `n` whole numbers in non-decreasing order. Print the different values on one line, separated by spaces, then `distinct: K`.

**Example**

Input (also in `in.txt`):
```
7
1 1 2 3 3 3 7
```
Output:
```
1 2 3 7
distinct: 4
```

**Focus:** in sorted data equal values are neighbours, so comparing with the previous element finds every repeat.
