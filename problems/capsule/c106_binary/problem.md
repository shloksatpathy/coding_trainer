# C106 · In binary

Read a whole number `n` ≥ 0 and print it in binary, without leading zeros (0 is `0`). Use recursion: first print `n / 2` in binary (if it is not 0), then the last bit `n % 2`.

**Example**

Input (also in `in.txt`):
```
5
```
Output:
```
101
```

**Focus:** recursion produces digits in the right order, where a loop would produce them backwards.
