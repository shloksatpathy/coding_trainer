# P53 · All permutations

Read `n` (n ≤ 7), then `n` distinct integers. Print all permutations in lexicographic order, one per line.

**Focus:** sort first, then backtrack with a `used[]` array. Afterwards compare with C++ `std::next_permutation` and write that algorithm yourself in Rust.

**Sample input** (also in `in.txt`):
```
3
3 1 2
```
