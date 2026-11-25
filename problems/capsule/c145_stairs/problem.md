# C145 · Climbing stairs

Read `n` (1 ≤ n ≤ 90). You climb a staircase of `n` steps, taking 1 or 2 steps at a time. Print the number of different ways to reach the top. Store the answers for smaller staircases in an array instead of recomputing them.

**Example**

Input (also in `in.txt`):
```
4
```
Output:
```
5
```

**Focus:** dynamic programming: ways(n) = ways(n - 1) + ways(n - 2), filled in from the bottom up. The plain recursion (like C102) would take years for n = 90.
