# C122 · Bubble sort

The first line has `n`; the second line has `n` whole numbers. (1 ≤ n ≤ 1000). Sort them with bubble sort: go through the array again and again, swapping neighbours that are in the wrong order, until a pass makes no swap. Print the sorted numbers on one line, then `swaps: K`, the total number of swaps.

**Example**

Input (also in `in.txt`):
```
5
5 1 4 2 8
```
Output:
```
1 2 4 5 8
swaps: 4
```

**Focus:** your first sorting algorithm, and counting the work it does: the swaps are exactly the pairs that were out of order.
