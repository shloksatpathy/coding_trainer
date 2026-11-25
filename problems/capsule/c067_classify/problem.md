# C067 · Return early

Write `classify(n)` that returns the word `negative`, `zero`, `small` (1 to 9), `medium` (10 to 99) or `large` (100 or more). Use a `return` for each case, with no `else`. The first line has `n`, the second `n` whole numbers: print the word for each, one per line.

**Example**

Input (also in `in.txt`):
```
6
-5 0 7 10 99 100
```
Output:
```
negative
zero
small
medium
medium
large
```

**Focus:** `return` ends the function at once, so each later check already knows the earlier ones were false.
