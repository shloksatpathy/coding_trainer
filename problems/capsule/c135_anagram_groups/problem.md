# C135 · Anagram groups

The first line has `n` (1 ≤ n ≤ 1000); the second has `n` words of lowercase letters (at most 20 letters each). Words are anagrams when they have the same letters, like `listen` and `silent`. Print one line per group of anagrams, in the order the groups first appear, with the words in input order separated by spaces.

**Example**

Input (also in `in.txt`):
```
6
listen enlist google silent gogole tinsel
```
Output:
```
listen enlist silent tinsel
google gogole
```

**Focus:** choosing a good key: sorting a word's letters gives the same key for all its anagrams.
