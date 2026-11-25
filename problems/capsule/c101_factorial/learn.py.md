**Learn · recursion**

A function may call itself. Each call works on a smaller problem, and a base case answers the smallest problem directly so that the calls stop.

```python
def countdown(n):
    if n == 0:
        print("go!")
        return
    print(n)
    countdown(n - 1)


countdown(3)
```

`countdown(3)` prints `3`, `2`, `1` and `go!`.
