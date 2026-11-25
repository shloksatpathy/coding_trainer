**Learn · records**

A class groups named values. With `@dataclass` (from `dataclasses`) you only list the fields and their types; `Point(3, 4)` creates one and `p.x` reads a field.

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(3, 4)
print(p.x + p.y)
```

prints `7`.
