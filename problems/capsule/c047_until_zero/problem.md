# C047 · Until zero

The input is whole numbers, one per line, ending with `0`. Print `count: K` and `sum: S` for the numbers before the 0 (the 0 itself doesn't count).

**Example**

Input (also in `in.txt`):
```
5
3
0
```
Output:
```
count: 2
sum: 8
```

**Focus:** a loop that stops on a special value (a sentinel) instead of after a known number of rounds.
