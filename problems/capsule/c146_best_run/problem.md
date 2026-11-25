# C146 · Best run

The first line has `n` (1 ≤ n ≤ 200 000); the second has `n` whole numbers (|x| ≤ 10^9). Print the largest sum of a run of one or more neighbouring numbers. The last test is too big to try every run.

**Example**

Input (also in `in.txt`):
```
8
-2 1 -3 4 -1 2 1 -5
```
Output:
```
6
```

**Focus:** one pass with a running best: the best run ending here is either this number alone or this number added to the best run ending just before.
