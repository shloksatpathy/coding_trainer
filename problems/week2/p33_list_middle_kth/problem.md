# P33 · Middle and k-th from end

Read `n k` (1 ≤ k ≤ n), then `n` integers. Build a linked list. Print the middle value (the second middle when n is even) using slow/fast pointers, and the k-th value from the end using two pointers k apart. Output: `middle kth`.

**Focus:** one pass each, no length count. Fast moves 2 steps, slow moves 1.

**Sample input** (also in `in.txt`):
```
5 2
1 2 3 4 5
```
