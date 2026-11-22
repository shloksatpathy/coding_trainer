# P62 · k largest elements

Read `n k` (1 ≤ k ≤ n), then `n` integers. Print the k largest values in descending order.

**Analysis:** keep a min-heap of size k: push each value, pop when the size exceeds k. O(n log k). Use your own heap in C, `std::priority_queue<int, vector<int>, greater<int>>` in C++, `heapq` in Python, `BinaryHeap<Reverse<i64>>` in Rust.

**Sample input** (also in `in.txt`):
```
6 3
3 1 5 12 2 11
```
