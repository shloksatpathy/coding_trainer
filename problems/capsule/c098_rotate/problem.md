# C098 · Rotate a picture

The first line has `r` and `c` (1 ≤ r, c ≤ 100); then come `r` lines of `c` characters each, with no spaces. Print the picture rotated 90° clockwise: `c` lines of `r` characters. The first output row is the first input column, read from the bottom up.

**Example**

Input (also in `in.txt`):
```
2 3
abc
def
```
Output:
```
da
eb
fc
```

**Focus:** working out where each cell goes: output row `j`, column `k` comes from input row `r - 1 - k`, column `j`.
