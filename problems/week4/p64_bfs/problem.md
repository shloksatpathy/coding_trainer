# P64 · Breadth-first search

Read an undirected graph, then a start vertex `s` on the last line. Print the BFS visiting order from `s`, visiting neighbours in increasing order.

Graph input: `n m` (vertices 1..n, m edges), then m lines `u v`.

**Focus:** adjacency lists (C: arrays + counts, or a CSR layout; C++: `vector<vector<int>>`; Rust: `Vec<Vec<usize>>`), sort each list, a queue and a `visited` array. **Rust:** `VecDeque<usize>`.

**Sample input** (also in `in.txt`):
```
6 6
1 2
1 3
2 4
3 4
4 5
5 6
1
```
