# C076 · Running totals

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. Print the running totals on one line, separated by spaces: the first number, the sum of the first two, of the first three, and so on.

**Example**

Input (also in `in.txt`):
```
5
1 2 3 4 5
```
Output:
```
1 3 6 10 15
```

**Focus:** each total is the previous total plus one number: one loop, no inner loop.
