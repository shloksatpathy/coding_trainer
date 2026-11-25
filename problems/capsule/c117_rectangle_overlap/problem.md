# C117 · Overlapping rectangles

Each of the two input lines describes a rectangle by its corners `x1 y1 x2 y2`, with x1 < x2 and y1 < y2. Store them in a `Rect` record and write `overlap_area(a, b)`. Print the area that the two rectangles have in common (0 if they only touch or don't meet).

**Example**

Input (also in `in.txt`):
```
0 0 4 3
2 1 6 5
```
Output:
```
4
```

**Focus:** a function on two records; the overlap in one direction runs from the larger start to the smaller end, if that is positive.
