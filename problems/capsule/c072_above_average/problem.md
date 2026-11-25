# C072 · Above average

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. Print `average: X` with 2 decimals, then on a second line the numbers that are strictly above the average, in input order and separated by spaces, or `none`.

**Example**

Input (also in `in.txt`):
```
5
1 2 3 4 5
```
Output:
```
average: 3.00
4 5
```

**Focus:** why arrays exist: the average is only known after reading everything, so the numbers must be kept to look at them again. Comparing `x * n > sum` avoids decimals altogether.
