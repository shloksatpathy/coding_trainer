# C110 · Checkpoint: permutations

Read `n` (1 ≤ n ≤ 6). Print every ordering of the numbers 1 to `n`, one per line with the numbers separated by spaces, in increasing (dictionary) order.

**Example**

Input (also in `in.txt`):
```
3
```
Output:
```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

**Focus:** checkpoint for module 11: backtracking with a "used" array: pick an unused number for this position, recurse, then free it again.
