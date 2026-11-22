# P61 · Build a heap, then heapsort

Read `n`, then `n` integers. Build a max-heap in the array bottom-up: call `sift_down(i)` for i = n/2 − 1 down to 0. Print the array. Then heapsort: repeatedly swap the root with the last element of the heap, shrink the heap by one and sift the root down. Print the sorted array.

`sift_down` moves to the larger child (the left one if they are equal) and swaps only while that child is strictly larger.

**Analysis:** bottom-up heap building is O(n), not O(n log n). Children of i are `2i+1` and `2i+2`.

**Sample input** (also in `in.txt`):
```
5
4 10 3 5 1
```
