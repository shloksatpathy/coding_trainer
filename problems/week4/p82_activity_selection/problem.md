# P82 · Activity selection

Read `n`, then n lines `start end`. Print the maximum number of activities you can attend without overlap. An activity may start exactly when the previous one ends.

**Analysis:** greedy — sort by end time and take every activity that starts after the last chosen one ends. Prove it to yourself: the earliest-ending activity is always safe to take.

**Sample input** (also in `in.txt`):
```
6
1 2
3 4
0 6
5 7
8 9
5 9
```
