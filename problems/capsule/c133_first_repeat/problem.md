# C133 · First repeat

The first line has `n` (1 ≤ n ≤ 200 000); the second has `n` whole numbers (|x| ≤ 10^9). Going from left to right, print the first value that appears for the second time, or `none`. The last test is too big to compare every pair.

**Example**

Input (also in `in.txt`):
```
6
5 3 8 3 5 1
```
Output:
```
3
```

**Focus:** a set turns "have I seen this before?" into one quick step, so the whole input is one pass.
