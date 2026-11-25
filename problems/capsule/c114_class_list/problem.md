# C114 · Class list

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines has a name (one word) and a whole-number score. Print `top: NAME (S)` for the best score (the first student if tied), `average: X` with 2 decimals, and `above: …` with the names of the students strictly above the average, in input order and separated by spaces, or `above: none`.

**Example**

Input (also in `in.txt`):
```
4
ann 90
bob 72
cy 90
dee 60
```
Output:
```
top: ann (90)
average: 78.00
above: ann cy
```

**Focus:** an array of records: one element per student, each with its own fields.
