# P75 · Coin change: number of ways

Read `k amount`, then `k` coin values. Print the number of different combinations of coins that make `amount` (order doesn't matter: `1+2` and `2+1` are the same).

**Analysis:** loop over coins on the outside and amounts on the inside — swapping the loops counts ordered sequences instead. Try both and compare on the sample.

**Sample input** (also in `in.txt`):
```
3 5
1 2 5
```
