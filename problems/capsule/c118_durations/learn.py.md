**Learn · reading values with separators**

`text.split(":")` splits at every `:` instead of at spaces.

```python
h, m = "09:15".split(":")
print(int(h), int(m))
```

prints `9 15`.
