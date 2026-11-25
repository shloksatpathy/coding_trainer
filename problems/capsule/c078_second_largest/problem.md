# C078 · Second largest

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. Print the second largest **different** value, or `none` if all the numbers are equal.

**Example**

Input (also in `in.txt`):
```
5
3 9 2 9 7
```
Output:
```
7
```

**Focus:** tracking two best values in one pass, and what "different" means when values repeat.
