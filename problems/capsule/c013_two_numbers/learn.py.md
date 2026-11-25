**Learn · reading two numbers**

`input().split()` cuts a line into words; `map(int, ...)` turns each word into a number.

```python
w, h = map(int, input().split())
print(w * h)
```

With the input `4 5` this prints `20`.
