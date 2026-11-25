**Learn · stacks**

A list works as a stack: `s.append(x)` puts on top, `s[-1]` is the top, `s.pop()` takes it off.

```python
s = []
s.append(1)
s.append(2)
print(s.pop(), s.pop())
```

The last value pushed comes off first.
