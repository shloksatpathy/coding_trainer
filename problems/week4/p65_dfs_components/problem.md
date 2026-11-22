# P65 · Depth-first search and components

Read an undirected graph, then a start vertex `s`. Print the recursive DFS visiting order from `s` (neighbours in increasing order), then `components=K`, the number of connected components of the whole graph.

Graph input: `n m` (vertices 1..n, m edges), then m lines `u v`.

**Focus:** recursive DFS, then loop over all vertices starting a new DFS from each unvisited one to count components. Deep recursion can overflow the stack on long paths — rewrite it with an explicit stack afterwards.

**Sample input** (also in `in.txt`):
```
7 6
1 2
1 3
2 4
3 4
4 5
5 6
1
```
