# P73 · Climbing stairs

Read `n` (1 ≤ n ≤ 90). You climb 1 or 2 steps at a time. Print the number of distinct ways to reach step n.

**Analysis:** `ways(n) = ways(n-1) + ways(n-2)`. Plain recursion is O(2ⁿ) — try n = 45 and watch it crawl. Memoization or a bottom-up loop with two variables is O(n). The answer for n = 90 needs 64 bits.

**Sample input** (also in `in.txt`):
```
5
```
