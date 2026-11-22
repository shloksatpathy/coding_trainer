# P26 · Selection sort, pass by pass

Read `n` (n ≥ 2), then `n` integers. Run selection sort: in pass i (i = 0 .. n-2) find the index of the minimum of `a[i..n-1]` (leftmost one on ties) and swap it with `a[i]`. Print the array after every pass.

**Focus:** exactly n-1 passes and at most n-1 swaps, but always O(n²) comparisons. In Rust, use `a.swap(i, m)`.

**Sample input** (also in `in.txt`):
```
4
64 25 12 22
```
