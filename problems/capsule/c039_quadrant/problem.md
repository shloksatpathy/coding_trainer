# C039 · Quadrant

Read the coordinates `x y` of a point (whole numbers). Print `Q1` (x > 0, y > 0), `Q2` (x < 0, y > 0), `Q3` (x < 0, y < 0) or `Q4` (x > 0, y < 0). A point on an axis is in no quadrant: print `origin` for (0, 0), `x-axis` when only y is 0 and `y-axis` when only x is 0.

**Example**

Input (also in `in.txt`):
```
1 1
```
Output:
```
Q1
```

**Focus:** nested decisions: an `if` inside another `if`.
