# C138 · Phone book

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines has a name and a number (one word each; names are different). Then comes `q`, and `q` names, one per line. For each, print `NAME: NUMBER`, or `NAME: not found`.

**Example**

Input (also in `in.txt`):
```
3
ann 555-0101
bob 555-0102
cy 555-0103
3
bob
dan
ann
```
Output:
```
bob: 555-0102
dan: not found
ann: 555-0101
```

**Focus:** a map from text to text: build it once, then answer each question with one lookup.
