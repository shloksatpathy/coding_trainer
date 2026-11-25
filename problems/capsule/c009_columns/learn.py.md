**Learn · fixed widths**

In an f-string, `{value:<8}` pads the value to 8 characters, aligned left; `{value:>4}` aligns right.

```python
print(f"{'pear':<8}|{7:>4}|")
```

prints `pear    |   7|`.
