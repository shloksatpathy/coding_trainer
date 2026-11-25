# C016 · Swap two variables

Read two whole numbers `a` and `b`. Print `before: a=A b=B`. Then swap the values of the two variables using a third variable, and print `after: a=A b=B` from the same two variables.

**Example**

Input (also in `in.txt`):
```
1 2
```
Output:
```
before: a=1 b=2
after: a=2 b=1
```

**Focus:** `a = b` copies the value of `b` into `a`, and the old value of `a` is gone. Keep it in a temporary variable first.
