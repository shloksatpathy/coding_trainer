# P39 · Next greater element

Read `n`, then `n` integers. For each element print the first element to its right that is strictly greater, or `-1`.

Sample: `4 5 2 25` → `5 25 25 -1`

**Analysis:** the double loop is O(n²) and too slow for the 100,000-number test. A monotonic stack of indices gives O(n): each index is pushed and popped once.

**Sample input** (also in `in.txt`):
```
4
4 5 2 25
```
