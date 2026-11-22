# P83 · Jump game

Read `n`, then `n` non-negative integers; `a[i]` is the longest jump from index i. Starting at index 0, print the fewest jumps to reach index n − 1, or `-1` if it can't be reached.

Samples: `2 3 1 1 4` → `2` · `3 2 1 0 4` → `-1`

**Analysis:** greedy BFS by layers: track the end of the current jump's reach and the farthest index reachable from it. O(n), versus O(n²) DP.

**Sample input** (also in `in.txt`):
```
5
2 3 1 1 4
```
