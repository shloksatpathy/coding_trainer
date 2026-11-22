# P69 · Topological sort

Read a directed graph: `n m`, then m lines `u v` meaning u must come before v. Print a topological order using Kahn's algorithm that always takes the **smallest-numbered** vertex with in-degree 0. If the graph has a cycle, print `Cycle`.

**Focus:** in-degree array + a min-priority queue. If fewer than n vertices come out, there is a cycle. **Rust:** `BinaryHeap<Reverse<usize>>`.

**Sample input** (also in `in.txt`):
```
6 6
6 3
6 1
5 1
5 2
3 4
4 2
```
