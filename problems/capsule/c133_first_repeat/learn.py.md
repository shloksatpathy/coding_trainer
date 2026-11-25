**Learn · fast lookups: hashing**

Sets and dictionaries are hash tables: a key's hash says where to store it, so checking it costs about one step however big the set is.

```python
seen = set()
for x in [4, 8, 4]:
    print(x in seen)
    seen.add(x)
```

prints no, no, yes (as false/true or 0/1).
