# C105 · Backwards, recursively

Read a word and print it backwards, without loops: a recursive function for position `i` first handles the rest of the word (from `i + 1`) and then prints the character at `i`.

**Example**

Input (also in `in.txt`):
```
hello
```
Output:
```
olleh
```

**Focus:** using the return trip of recursion to reverse an order.
