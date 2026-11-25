# C108 · All binary strings

Read `n` (1 ≤ n ≤ 10). Print every string of `n` characters made of `0` and `1`, in increasing order (`00…0` first), one per line.

**Example**

Input (also in `in.txt`):
```
2
```
Output:
```
00
01
10
11
```

**Focus:** backtracking: choose a character for this position, let recursion fill the rest, then try the other choice.
