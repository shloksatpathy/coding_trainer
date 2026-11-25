# C136 · Set operations

The first line has `n` and then `n` whole numbers; the second line has `m` and then `m` whole numbers (1 ≤ n, m ≤ 1000). Treating each line as a set of values (repeats count once), print three lines:

```
union: …
both: …
only first: …
```

each with its values in increasing order separated by spaces, or `none`.

**Example**

Input (also in `in.txt`):
```
5 1 2 3 3 4
4 3 4 5 6
```
Output:
```
union: 1 2 3 4 5 6
both: 3 4
only first: 1 2
```

**Focus:** union, intersection and difference of sets; sorted output makes the order well-defined.
