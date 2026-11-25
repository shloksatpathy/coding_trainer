**Learn · a loop inside a loop**

The inner loop runs all its rounds for each round of the outer loop.

```python
for row in range(1, 3):
    for col in range(1, 4):
        print(f"{row}{col} ", end="")
    print()
```

prints `11 12 13` on the first line and `21 22 23` on the second.
