**Learn · characters as numbers**

`ord(ch)` gives a character's code number and `chr(n)` turns a code back into a character. The letters have consecutive codes, so `ord("c") - ord("a")` is 2.

```python
print(chr(ord("a") + 2))
```

prints `c`.
