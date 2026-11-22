# P78 · Edit distance

Read two words on one line. Print the minimum number of single-character insertions, deletions and replacements that turn the first into the second (Levenshtein distance).

Sample: `horse ros` → `3`

**Analysis:** `dp[i][j] = dp[i-1][j-1]` if the characters match, else `1 + min(insert, delete, replace)`. Fill the first row and column with 0..n and 0..m first.

**Sample input** (also in `in.txt`):
```
horse ros
```
