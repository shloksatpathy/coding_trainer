# C037 · Triangle

Read three whole numbers, the sides of a triangle. Print `not a triangle` if any side is 0 or less, or if one side is at least as long as the other two together. Otherwise print `equilateral` (all sides equal), `isosceles` (exactly two equal) or `scalene` (all different).

**Example**

Input (also in `in.txt`):
```
3 4 5
```
Output:
```
scalene
```

**Focus:** checking that the input makes sense first, then deciding between the remaining cases.
