# P74 · Coin change: fewest coins

Read `k amount`, then `k` coin values. Print the fewest coins that add up to `amount` (unlimited coins of each value), or `-1` if impossible.

**Analysis:** greedy (take the biggest coin first) fails for coins `1 3 4`, amount `6` — try it. DP: `best[x] = 1 + min(best[x - c])`. O(k · amount).

**Sample input** (also in `in.txt`):
```
3 11
1 2 5
```
