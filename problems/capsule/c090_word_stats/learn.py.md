**Learn · keeping a copy of a word**

Assigning text to another variable keeps it: `best = w` still holds the word after `w` changes.

```python
best = ""
for w in ["hi", "hello"]:
    best = w
print(best)
```

keeps the last word.
