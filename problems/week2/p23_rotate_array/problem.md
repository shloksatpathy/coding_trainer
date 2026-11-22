# P23 · Rotate an array in place

Read `n k` (k ≥ 0, k may be larger than n), then `n` integers. Rotate the array right by `k` positions in place using three reversals — no second array. Print it.

**Focus:** write a `reverse(a, i, j)` helper with two pointers. In C pass `int *a`, in Rust pass `&mut [i64]`. Remember `k %= n`.

**Sample input** (also in `in.txt`):
```
5 2
1 2 3 4 5
```
