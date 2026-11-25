**Learn · skipping a round with continue**

`continue` skips the rest of this round and goes on with the next one.

```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
```

prints only the odd numbers 1, 3, 5, 7, 9.
