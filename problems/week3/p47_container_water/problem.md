# P47 · Container with most water

Read `n`, then `n` non-negative heights. Choose two lines i < j to maximize `min(h[i], h[j]) * (j - i)`. Print that area.

Sample: `1 8 6 2 5 4 8 3 7` → `49`

**Analysis:** start with the widest pair and always move the shorter side inwards — O(n). Argue to yourself why moving the taller side can never help.

**Sample input** (also in `in.txt`):
```
9
1 8 6 2 5 4 8 3 7
```
