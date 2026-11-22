# P25 · Bubble sort with early exit

Read `n`, then `n` integers. Sort them ascending with bubble sort: pass i (i = 0, 1, ...) compares `a[j]` and `a[j+1]` for j = 0 .. n-2-i and swaps when `a[j] > a[j+1]`. Stop after the first pass that makes no swaps (or after pass n-2).

Print the sorted array, then `swaps=S passes=P`.

**Focus:** the swap count equals the number of inversions. An already sorted array needs only 1 pass — that is the best case O(n).

**Sample input** (also in `in.txt`):
```
5
5 1 4 2 8
```
