# P63 · Running median

Read `n`, then `n` integers. After reading each one, print the median of everything read so far with exactly 1 decimal: the middle value for an odd count, the average of the two middle values for an even count.

**Analysis:** two heaps — a max-heap for the lower half and a min-heap for the upper half, sizes differing by at most one. Each step is O(log n); re-sorting each time would be O(n² log n).

**Sample input** (also in `in.txt`):
```
5
5 15 1 3 8
```
