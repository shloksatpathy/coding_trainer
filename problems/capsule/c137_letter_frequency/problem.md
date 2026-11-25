# C137 · Letter frequency

Read one line of text. Counting uppercase and lowercase as the same letter, print each letter that appears as `letter: count` (lowercase letter), from the most frequent to the least, and alphabetically among equal counts. Other characters are ignored.

**Example**

Input (also in `in.txt`):
```
Hello World
```
Output:
```
l: 3
o: 2
d: 1
e: 1
h: 1
r: 1
w: 1
```

**Focus:** when the keys are a small fixed range (26 letters), an array indexed by the key is the simplest map.
