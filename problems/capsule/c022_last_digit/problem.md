# C022 · Last digit

Read a whole number `n` ≥ 0. Print `last digit: D` and `without it: W`, where D is the last digit of n and W is n with that digit removed.

**Example**

Input (also in `in.txt`):
```
1234
```
Output:
```
last digit: 4
without it: 123
```

**Focus:** `% 10` gives the last digit and `/ 10` removes it: the two tools for taking a number apart.
