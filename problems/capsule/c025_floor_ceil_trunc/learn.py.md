**Learn · decimal to whole number**

`math.floor` rounds down and `math.ceil` rounds up (both need `import math`); `int(x)` cuts off the fraction, which rounds toward zero.

```python
import math

x = -3.5
print(math.floor(x), math.ceil(x), int(x))
```

prints `-4 -3 -3`.
