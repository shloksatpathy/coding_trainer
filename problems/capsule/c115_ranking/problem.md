# C115 · Ranking

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines has a name (one word) and a whole-number score. Print the ranking: sorted by score from high to low, and by name alphabetically when scores are equal. Each line is `R. NAME SCORE`, with R counting from 1. Use your language's sort function with your own comparison.

**Example**

Input (also in `in.txt`):
```
4
ann 90
bob 85
cy 90
dee 70
```
Output:
```
1. ann 90
2. cy 90
3. bob 85
4. dee 70
```

**Focus:** sorting records with a custom rule: compare by the first key, and use the second key only when the first is equal.
