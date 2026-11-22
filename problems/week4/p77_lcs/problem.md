# P77 · Longest common subsequence

Read two strings (no spaces) on one line. Print the length of their longest common subsequence.

Sample: `abcde ace` → `3`

**Analysis:** `dp[i][j]` = LCS of the first i and first j characters; O(n·m) time. Then reduce memory to two rows. In Rust, index bytes (`s.as_bytes()`), not chars.

**Sample input** (also in `in.txt`):
```
abcde ace
```
