# C134 · Two sum

The first line has `n` (1 ≤ n ≤ 200 000) and a target `t`; the second has `n` whole numbers (|x| ≤ 10^9). Find positions `i < j` with `a[i] + a[j] = t`: the smallest such `j`, and for it the smallest `i`. Print `i j` counting from 1, or `none`.

**Example**

Input (also in `in.txt`):
```
5 9
2 7 11 15 -2
```
Output:
```
1 2
```

**Focus:** a map from value to its first position: for each element, ask whether its partner `t - a[j]` has already been seen.
