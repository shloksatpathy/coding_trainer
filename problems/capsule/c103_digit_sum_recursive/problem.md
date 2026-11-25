# C103 · Digit sum, recursively

Write a recursive `digit_sum(n)` for n ≥ 0, without loops: the last digit plus the digit sum of the rest. Read `n` and print `digit_sum(n)`.

**Example**

Input (also in `in.txt`):
```
1234
```
Output:
```
10
```

**Focus:** the base case doesn't have to be 0 calls deep: here a one-digit number is its own digit sum.
