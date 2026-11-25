**Learn · returning early, returning text**

A `return` ends the function at once, so the checks after it need no `else`.

```python
def size(n):
    if n < 10:
        return "short"
    return "long"
```
