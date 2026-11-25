**Learn · words**

`text.split()` (with nothing between the parentheses) splits at any run of spaces and ignores spaces at the ends; it gives a list of words.

```python
for w in "  to be  ".split():
    print(w)
```

prints `to` and `be` on two lines.
