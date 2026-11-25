# C148 · CSV totals

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines is a CSV record `name,department,amount` (no spaces; the amount is a whole number). Print the total amount per department as `department: total`, in the order the departments first appear, then `overall: T`.

**Example**

Input (also in `in.txt`):
```
4
ann,sales,100
bob,it,250
cy,sales,50
dee,hr,75
```
Output:
```
sales: 150
it: 250
hr: 75
overall: 475
```

**Focus:** parsing a line by a separator, then grouping and summing by a key.
