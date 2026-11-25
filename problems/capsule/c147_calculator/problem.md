# C147 · Calculator

Read one line: whole numbers and the operators `+`, `-` and `*`, all separated by spaces, like `2 + 3 * 4`. Print its value, with `*` done before `+` and `-`. All intermediate values fit in 64 bits.

**Example**

Input (also in `in.txt`):
```
2 + 3 * 4
```
Output:
```
14
```

**Focus:** parsing: reading tokens one at a time and keeping just enough state (the finished sum and the current product) to respect precedence.
