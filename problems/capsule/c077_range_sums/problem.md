# C077 · Range sums

The first line has `n` (1 ≤ n ≤ 1000); the second line has `n` whole numbers. Then comes `q`, and `q` lines with two positions `l r` (1 ≤ l ≤ r ≤ n). For each, print the sum of the numbers from position `l` to `r`, counting from 1.

Build an array of running totals `p` with `p[0] = 0` and `p[i]` = the sum of the first `i` numbers. Then each answer is `p[r] - p[l - 1]`, with no loop per question.

**Example**

Input (also in `in.txt`):
```
5
1 2 3 4 5
3
1 5
2 4
3 3
```
Output:
```
15
9
3
```

**Focus:** prefix sums: some work up front makes every later question instant.
