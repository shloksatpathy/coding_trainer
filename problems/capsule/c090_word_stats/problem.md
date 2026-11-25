# C090 · Checkpoint: word statistics

Read one line of words (letters only), separated by one or more spaces. Print four lines:

```
words: W
longest: WORD
shortest: WORD
average: X
```

with the first word when several share the longest or shortest length, and the average word length with 2 decimals. The line has at least one word.

**Example**

Input (also in `in.txt`):
```
the quick brown fox
```
Output:
```
words: 4
longest: quick
shortest: the
average: 4.00
```

**Focus:** checkpoint for module 9: splitting into words, lengths, keeping a copy of the best word so far, and a decimal average.
