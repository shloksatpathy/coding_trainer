# C040 · Checkpoint: grade

Read a score. If it is below 0 or above 100, print `invalid`. Otherwise print the letter and the result on one line, like `B pass`:

```
score 90-100  A
score 80-89   B
score 70-79   C
score 60-69   D
score 0-59    F
```

A score of 60 or more is a `pass`, below that a `fail`.

**Example**

Input (also in `in.txt`):
```
85
```
Output:
```
B pass
```

**Focus:** checkpoint for module 4: validating input, a chain of ranges and a second, separate decision.
