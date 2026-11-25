# C120 · Checkpoint: inventory report

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines has an item name (one word, at most 10 letters), a price in cents and a quantity. Print one line per item, sorted by line total (price × quantity) from high to low and by name when equal: the name left-aligned in 10 characters, the quantity right-aligned in 5, and the line total in dollars right-aligned in 10 (`D.CC`). Then print `TOTAL` left-aligned in 15 characters followed by the grand total right-aligned in 10.

**Example**

Input (also in `in.txt`):
```
3
apple 50 3
bread 250 2
milk 120 1
```
Output:
```
bread         2      5.00
apple         3      1.50
milk          1      1.20
TOTAL                7.70
```

**Focus:** checkpoint for module 12: records, a custom sort, and formatted output. Money stays in whole cents: print `cents / 100`, a point, and `cents % 100` with two digits.
