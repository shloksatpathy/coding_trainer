# P29 · Quick sort (Lomuto partition)

Read `n`, then `n` integers. Sort with quicksort using the Lomuto partition: pivot = last element of the range, `i = lo - 1`, for each j in lo..hi-1 if `a[j] <= pivot` then `i++` and swap `a[i], a[j]`; finally swap `a[i+1], a[hi]`. Recurse on both sides; only call partition when `lo < hi`.

Print the array after the very first partition, then the sorted array, then `partitions=K` (number of partition calls).

**Analysis:** try a sorted input of 2,000 numbers and count partitions — that is the O(n²) worst case of a last-element pivot.

**Sample input** (also in `in.txt`):
```
7
7 2 1 6 8 5 3
```
