# P43 · Two sum

Read `n target`, then `n` integers. Exactly one pair of indices i < j has `a[i] + a[j] == target`. Print `i j` (0-based).

**Analysis:** checking all pairs is O(n²) — too slow for the 100,000-number test. One pass with a hash map from value to index is O(n). C has no hash map: write a small open-addressing table, or sort (value, index) pairs and use two pointers. **Rust:** `HashMap<i64, usize>`.

**Sample input** (also in `in.txt`):
```
4 9
2 7 11 15
```
