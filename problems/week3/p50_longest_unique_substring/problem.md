# P50 · Longest substring without repeats

Read a string with no spaces (ASCII letters and digits). Print the length of its longest substring with no repeated characters.

Samples: `abcabcbb` → `3` · `bbbbb` → `1` · `pwwkew` → `3`

**Analysis:** a variable window `[lo, i]` plus a table of each character's last position; jump `lo` past the previous occurrence. O(n).

**Sample input** (also in `in.txt`):
```
abcabcbb
```
