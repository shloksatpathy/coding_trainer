# C109 · Subset sums

The first line has `n` and a target `t` (1 ≤ n ≤ 20, t ≥ 0); the second has `n` whole numbers ≥ 0. Print how many subsets (choices of some of the positions, possibly none) add up to exactly `t`.

**Example**

Input (also in `in.txt`):
```
4 5
1 2 3 4
```
Output:
```
2
```

**Focus:** every element is either left out or taken: two recursive calls per element explore all 2^n choices.
