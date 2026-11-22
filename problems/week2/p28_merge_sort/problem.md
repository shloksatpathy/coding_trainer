# P28 · Merge sort and inversion count

Read `n`, then `n` integers. Sort them with merge sort and count inversions (pairs i < j with a[i] > a[j]) during the merge step. Print the sorted array, then `inversions=K`.

**Analysis:** the last test has 50,000 numbers. O(n²) counting is too slow there; merge sort's O(n log n) is not. Inversions can exceed 2³¹ — use 64-bit counters. **Rust:** split with `split_at`, merge into a new `Vec`.

**Sample input** (also in `in.txt`):
```
5
2 4 1 3 5
```
