# C021 · Divide and remainder

Read two whole numbers `a` and `b` (a ≥ 0, b > 0). Print three lines:

```
a / b = Q
a % b = R
Q * b + R = A
```

where Q is the whole-number quotient, R the remainder, and the last line checks them.

**Example**

Input (also in `in.txt`):
```
7 2
```
Output:
```
a / b = 3
a % b = 1
Q * b + R = 7
```

**Focus:** whole-number division drops the fraction; the remainder is what is left over. Together they give back `a`.
