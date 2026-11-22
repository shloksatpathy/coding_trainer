# P30 · k-th smallest (quickselect)

Read `n k` (1 ≤ k ≤ n), then `n` integers. Print the k-th smallest value.

**Analysis:** sorting is O(n log n); quickselect (partition, then recurse into one side only) is O(n) on average. Implement quickselect — pick a random pivot so sorted inputs don't hit the worst case. Compare with `std::nth_element` and Rust's `select_nth_unstable`.

**Sample input** (also in `in.txt`):
```
6 2
7 10 4 3 20 15
```
