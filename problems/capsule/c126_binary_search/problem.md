# C126 · Binary search

The first line has `n` (1 ≤ n ≤ 200 000); the second has `n` different whole numbers in increasing order. Then comes `q` and a line of `q` values. For each value print its position (counting from 1), or `-1` if it isn't there, one per line. Write the binary search yourself; the last test is too big to check every element for every value.

**Example**

Input (also in `in.txt`):
```
5
1 3 5 7 9
4
7 1 4 10
```
Output:
```
4
1
-1
-1
```

**Focus:** binary search: compare with the middle of the remaining range and throw away the half that can't contain the value. 200 000 elements need at most 18 steps.
