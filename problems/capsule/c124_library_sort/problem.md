# C124 · Sorting with the library

The first line has `n`; the second line has `n` whole numbers. (1 ≤ n ≤ 200 000). Print them sorted from small to large on one line, then from large to small on a second line. Use your language's sort function: the last test is too big for bubble sort.

**Example**

Input (also in `in.txt`):
```
5
3 -1 4 1 5
```
Output:
```
-1 1 3 4 5
5 4 3 1 -1
```

**Focus:** the library sort takes about n·log n steps instead of n²: for 200 000 numbers that is millions of steps instead of tens of billions.
