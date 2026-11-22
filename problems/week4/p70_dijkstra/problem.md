# P70 · Dijkstra's shortest paths

Read a directed weighted graph: `n m`, then m lines `u v w` (w ≥ 0), then a source `s`. Print the shortest distance from s to every vertex 1..n on one line, `INF` for unreachable vertices.

**Analysis:** Dijkstra with a binary heap is O((n + m) log n). Skip stale heap entries (`if d > dist[u]: continue`). Distances can exceed 2³¹ — use 64-bit. **Rust:** `BinaryHeap<Reverse<(u64, usize)>>`.

**Sample input** (also in `in.txt`):
```
5 6
1 2 4
1 3 1
3 2 2
2 4 1
3 4 5
4 5 3
1
```
