**Learn · reading many values**

`input().split()` gives a list of the words on a line; `for w in words:` goes through them one by one.

```python
n = int(input())
words = input().split()
total = 0
for w in words:
    total += int(w)
print(total)
```

With the input `3` and `4 5 6` this prints the sum, `15`.
