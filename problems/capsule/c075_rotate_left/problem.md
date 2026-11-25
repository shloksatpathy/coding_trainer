# C075 · Rotate left

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. The third line has `k` ≥ 0. Rotate the numbers `k` places to the left: each step moves the first number to the end. Print the result on one line, separated by spaces. `k` can be larger than `n`.

**Example**

Input (also in `in.txt`):
```
5
1 2 3 4 5
2
```
Output:
```
3 4 5 1 2
```

**Focus:** index arithmetic: after rotating, position `i` holds the element from position `(i + k) % n`.
