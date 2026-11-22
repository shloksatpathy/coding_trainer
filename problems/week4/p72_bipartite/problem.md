# P72 · Bipartite check

Read an undirected graph (possibly disconnected). Print `Yes` if its vertices can be coloured with two colours so that every edge joins different colours, else `No`.

Graph input: `n m` (vertices 1..n, m edges), then m lines `u v`.

**Focus:** BFS from every uncoloured vertex, giving neighbours the opposite colour; a same-colour edge means an odd cycle.

**Sample input** (also in `in.txt`):
```
4 4
1 2
2 3
3 4
4 1
```
