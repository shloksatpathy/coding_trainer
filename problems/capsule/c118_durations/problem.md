# C118 · Durations

The input is two times of the same day, `HH:MM HH:MM`, the second not earlier than the first. Store each in a `Time` record (hours, minutes) and write `to_minutes(t)`. Print the time between them as `H:MM`.

**Example**

Input (also in `in.txt`):
```
09:15 17:45
```
Output:
```
8:30
```

**Focus:** parsing input with a separator other than a space, and converting a record into one number to compute with it.
