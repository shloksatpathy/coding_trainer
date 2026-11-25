# C055 · Times table

Read `n` (1 ≤ n ≤ 12). Print the `n` × `n` times table: row `r`, column `c` holds `r * c`, and every value is right-aligned in a field 4 characters wide.

**Example**

Input (also in `in.txt`):
```
3
```
Output:
```
   1   2   3
   2   4   6
   3   6   9
```

**Focus:** a table is rows of columns: nested loops plus the fixed-width formatting from C009.
