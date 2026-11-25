# C028 · Order of operations

Read three whole numbers `a b c` (all > 0). Print these four results, one per line:

```
a + b * c
(a + b) * c
a - b - c
a / b * c
```

The last one uses whole-number division.

**Example**

Input (also in `in.txt`):
```
2 3 4
```
Output:
```
14
20
-5
0
```

**Focus:** `*`, `/` and `%` go before `+` and `-`; operators of the same rank go from left to right; parentheses change the order.
