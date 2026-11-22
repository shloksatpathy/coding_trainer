# P12 · Tower of Hanoi

Read `n`. Move n disks from rod A to rod C using B as the helper. Print every move as `Move disk k from X to Y`, then a final line `Total moves: N`.

Sample input `2`:
```
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
Total moves: 3
```

**Analysis:** the move count is 2^n − 1. Confirm it from your program's output for n = 1 to 10.

**Sample input** (also in `in.txt`):
```
3
```
