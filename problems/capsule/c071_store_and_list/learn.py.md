**Learn · arrays and lists**

A list holds many values in order. `a = []` makes an empty list, `a.append(x)` adds `x` at the end, `a[i]` is the value at position `i` (counting from 0) and `len(a)` is the number of values.

```python
n = int(input())
a = []
for w in input().split():
    a.append(int(w))
print(a[0], len(a))
```

With the input `3` and `7 8 9` this prints `7 3`.
