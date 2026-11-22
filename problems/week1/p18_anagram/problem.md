# P18 · Anagram check

Read two lowercase words on one line. Print `Yes` if they are anagrams, else `No`.

Samples: `listen silent` → `Yes` · `rat car` → `No`

**Analysis:** a 26-slot count array is O(n). Sorting both words is O(n log n). Implement the count array in all 4 languages, then the sort version in Python as a cross-check.

**Sample input** (also in `in.txt`):
```
listen silent
```
