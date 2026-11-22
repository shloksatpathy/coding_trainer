# P24 · Remove duplicates from a sorted array

Read `n`, then `n` integers in non-decreasing order. Remove duplicates in place with a read pointer and a write pointer. Print the number of unique values on line 1 and the unique values on line 2.

**Focus:** O(n) time, O(1) extra memory. In Rust, compare with `v.dedup()` afterwards.

**Sample input** (also in `in.txt`):
```
7
1 1 2 3 3 3 4
```
