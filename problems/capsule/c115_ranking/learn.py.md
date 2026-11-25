**Learn · sorting with your own rule**

`list.sort(key=...)` sorts by the value the key function gives each element. `lambda s: (-s.score, s.name)` is a small unnamed function; tuples compare item by item, so this sorts by score from high to low (the minus), then by name.

```python
words = ["pear", "fig", "apple"]
words.sort(key=lambda w: (len(w), w))
print(words)
```
