# P27 · Insertion sort, step by step

Read `n` (n ≥ 2), then `n` integers. Run insertion sort: for i = 1 .. n-1, take `key = a[i]` and shift larger elements of the sorted prefix one place right, then drop `key` in. Print the array after every i, then `shifts=K` (total element shifts).

**Focus:** shifting, not swapping. Insertion sort is fast on nearly sorted input — try it.

**Sample input** (also in `in.txt`):
```
5
5 2 4 6 1
```
