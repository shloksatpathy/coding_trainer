# C131 · Word count

The first line has `n` (1 ≤ n ≤ 1000); the second has `n` words. Print each different word with the number of times it appears, as `word: count`, in the order the words first appear.

**Example**

Input (also in `in.txt`):
```
6
the cat and the hat the
```
Output:
```
the: 3
cat: 1
and: 1
hat: 1
```

**Focus:** a map (dictionary) stores a value for each key: here a count for each word. Looking a key up doesn't need a loop.
