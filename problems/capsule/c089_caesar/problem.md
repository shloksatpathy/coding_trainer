# C089 · Caesar cipher

The first line is a text, the second a shift `k` (0 ≤ k ≤ 25). Shift every letter `k` places forward in the alphabet, wrapping from `z` back to `a`; uppercase stays uppercase. Other characters stay as they are. The text has only plain English letters, digits, spaces and punctuation.

**Example**

Input (also in `in.txt`):
```
Hello, World!
3
```
Output:
```
Khoor, Zruog!
```

**Focus:** characters are small numbers: subtract `'a'` to get a letter's place (0 to 25), do arithmetic, add `'a'` back.
