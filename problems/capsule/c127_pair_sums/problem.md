# C127 · Pairs with a given sum

The first line has `n` (1 ≤ n ≤ 200 000) and a target `t`; the second has `n` different whole numbers in increasing order. Print every pair `a b` with `a < b` and `a + b = t`, one per line in increasing order of `a`, or `none`.

**Example**

Input (also in `in.txt`):
```
6 10
1 3 4 6 7 9
```
Output:
```
1 9
3 7
4 6
```

**Focus:** two pointers: start at both ends; if the sum is too small move the left one right, if too big move the right one left. One pass instead of trying every pair.
