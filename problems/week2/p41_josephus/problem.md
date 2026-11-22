# P41 · Josephus problem with a queue

Read `n k`. People 1..n stand in a circle. Starting from person 1, count k people; the k-th leaves. Counting continues from the next person. Print the order in which people leave (the last one is the survivor).

Sample: `7 3` → `3 6 2 7 5 1 4`

**Focus:** a queue: move k-1 people from front to back, then remove the front. Use your circular queue from P40 or `std::queue`, `collections.deque`, `VecDeque`.

**Sample input** (also in `in.txt`):
```
7 3
```
