# P71 · Minimum spanning tree (Kruskal)

Read an undirected weighted graph: `n m`, then m lines `u v w`. Print the total weight of a minimum spanning tree, or `Disconnected` if the graph is not connected.

**Focus:** sort edges by weight, add each edge whose endpoints are in different sets of a union-find (disjoint set union) with path compression. A tree on n vertices has n − 1 edges — that's your connectivity check.

**Sample input** (also in `in.txt`):
```
4 5
1 2 1
2 3 4
1 3 3
3 4 2
1 4 5
```
