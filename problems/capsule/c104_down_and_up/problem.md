# C104 · Down and up

Write a recursive function that, for `n`, prints `n`, then calls itself for `n - 1`, then prints `n` again (and does nothing for 0). Read `n` ≥ 1 and call it: the output counts down to 1 and back up, one number per line.

**Example**

Input (also in `in.txt`):
```
3
```
Output:
```
3
2
1
1
2
3
```

**Focus:** code after the recursive call runs when the call returns, in the opposite order: each call waits for the ones it started.
