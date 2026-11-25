# C079 · Tally

The first line has `n` (1 ≤ n ≤ 1000); the second has `n` values, each from 0 to 9. For every value that appears, in increasing order, print `value: count` on its own line.

**Example**

Input (also in `in.txt`):
```
8
3 1 4 1 5 9 2 6
```
Output:
```
1: 2
2: 1
3: 1
4: 1
5: 1
6: 1
9: 1
```

**Focus:** a counting array: the value itself is the index, so `count[v] += 1` tallies it in one step.
