# P14 · Reverse an array in place

Read `n`, then `n` integers. Reverse them in place with two pointers (no second array) and print them.

**Focus:** in Rust, use `v.swap(i, j)`. Try writing `let a = &mut v[i]; let b = &mut v[j];` first and read the compiler error. It shows the borrowing rule: only one mutable reference at a time.

**Sample input** (also in `in.txt`):
```
5
1 2 3 4 5
```
