# C038 · Ticket price

Read an age (a whole number ≥ 0). Print the ticket:

```
age 0-2          free
age 3-12         child 5
age 13-64        adult 12
age 65 and over  senior 7
```

**Example**

Input (also in `in.txt`):
```
30
```
Output:
```
adult 12
```

**Focus:** a chain of conditions on ranges. Each boundary age belongs to exactly one row.
