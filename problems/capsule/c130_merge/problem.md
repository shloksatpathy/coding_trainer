# C130 · Checkpoint: merge

The first line has `n`, the second `n` whole numbers in non-decreasing order; the third has `m`, the fourth `m` whole numbers in non-decreasing order (1 ≤ n, m ≤ 100 000). Print all `n + m` numbers in non-decreasing order on one line. Don't sort: merge the two lists by always taking the smaller front element.

**Example**

Input (also in `in.txt`):
```
3
1 4 9
4
2 3 4 10
```
Output:
```
1 2 3 4 4 9 10
```

**Focus:** checkpoint for module 13: two pointers walking two sorted lists, which is also the heart of merge sort.
