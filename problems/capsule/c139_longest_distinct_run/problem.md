# C139 · Longest run without repeats

Read one line of text. Print the length of the longest stretch of consecutive characters in which no character appears twice (spaces count as characters).

**Example**

Input (also in `in.txt`):
```
abcabcbb
```
Output:
```
3
```

**Focus:** a sliding window: remember where each character was last seen, and move the window's start past a repeat instead of starting over.
