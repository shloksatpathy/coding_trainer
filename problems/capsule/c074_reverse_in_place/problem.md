# C074 · Reverse in place

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. Reverse the array **in place**, by swapping the first and last elements, then the second and second-to-last, and so on, without a second array. Then print it on one line, separated by spaces.

**Example**

Input (also in `in.txt`):
```
5
1 2 3 4 5
```
Output:
```
5 4 3 2 1
```

**Focus:** two positions moving toward each other; stop in the middle, or every pair is swapped twice.
