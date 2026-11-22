# P52 · All subsets

Read `n` (1 ≤ n ≤ 10). Print every non-empty subset of {1, ..., n}, one per line with elements ascending, in lexicographic order.

Sample `3` → `1` / `1 2` / `1 2 3` / `1 3` / `2` / `2 3` / `3`

**Focus:** backtracking: `choose(start)` prints the current subset, then for each i ≥ start pushes i, recurses with i + 1, and pops. There are 2ⁿ − 1 lines.

**Sample input** (also in `in.txt`):
```
3
```
