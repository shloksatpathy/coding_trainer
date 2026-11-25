# C057 · Counting triangle

Read `n` ≥ 1. Print `n` lines: line `i` has `i` numbers, separated by single spaces. The numbers count up from 1 and carry on from one line to the next (1 / 2 3 / 4 5 6 / …).

**Example**

Input (also in `in.txt`):
```
4
```
Output:
```
1
2 3
4 5 6
7 8 9 10
```

**Focus:** a counter that lives outside both loops keeps its value from line to line.
