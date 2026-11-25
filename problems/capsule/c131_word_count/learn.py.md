**Learn · maps**

A dictionary maps keys to values: `d = {}`, `d[key] = value`, `key in d`, `d.get(key, 0)` (0 if the key is missing). Looping over a dictionary gives its keys in the order they were first added.

```python
age = {}
age["ann"] = 30
print("ann" in age, age.get("bob", 0))
```
