# P67 · Shortest path (unweighted)

Read an undirected graph, then `s t`. Print the length (in edges) of the shortest path from s to t, then the path itself. If t is unreachable print `-1`.

Run BFS from s visiting neighbours in increasing order; each vertex's parent is the vertex that discovered it. Rebuild the path by following parents back from t.

Graph input: `n m` (vertices 1..n, m edges), then m lines `u v`.

**Focus:** BFS gives shortest paths when all edges cost the same. Store `parent[]`, walk back from t, reverse.

**Sample input** (also in `in.txt`):
```
6 7
1 2
1 3
2 4
3 4
4 5
5 6
3 6
1 6
```
