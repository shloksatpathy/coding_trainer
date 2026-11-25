**Learn · looking at each character**

`for ch in text:` goes through the characters. `ch.isupper()` and `ch.islower()` test a character; `ch.upper()` and `ch.lower()` convert it.

```python
for ch in "a1B":
    if ch.isupper():
        print(ch, "is uppercase")
```

prints `B is uppercase`.
