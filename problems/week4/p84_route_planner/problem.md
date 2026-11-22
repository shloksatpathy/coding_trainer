# P84 · Mini-project: route planner

Read `m`, then m roads `CityA CityB km` (two-way), then `q`, then q queries `From To`. For each query print the shortest route as `km: A -> X -> B`, or `No route`. A city with no roads can still be queried; a query from a city to itself prints `0: A`. Shortest routes in the tests are unique.

Sample input:
```
4
Pune Mumbai 150
Pune Nashik 210
Mumbai Nashik 170
Nashik Indore 400
3
Mumbai Indore
Pune Pune
Pune Goa
```
Output:
```
570: Mumbai -> Nashik -> Indore
0: Pune
No route
```

**Focus:** this ties the course together: map names to ids with a hash map, store an adjacency list, run Dijkstra with a parent array and rebuild the path. **Rust:** a `struct Graph { ids: HashMap<String, usize>, names: Vec<String>, adj: Vec<Vec<(usize, u64)>> }` with `impl` methods, and `Option` for "No route".

**Sample input** (also in `in.txt`):
```
4
Pune Mumbai 150
Pune Nashik 210
Mumbai Nashik 170
Nashik Indore 400
3
Mumbai Indore
Pune Pune
Pune Goa
```
