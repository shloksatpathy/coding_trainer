# C123 · Insertion sort, step by step

The first line has `n`; the second line has `n` whole numbers. (1 ≤ n ≤ 100). Sort them with insertion sort: for `i` = 1, 2, …, n − 1, take element `i` and shift it left past every larger element before it. After each step `i`, print the whole array on one line.

**Example**

Input (also in `in.txt`):
```
4
3 1 4 2
```
Output:
```
1 3 4 2
1 3 4 2
1 2 3 4
```

**Focus:** insertion sort keeps the left part sorted and inserts one more element into it each step.
