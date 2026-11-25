# C111 · Points

Store two points in a record type `Point` with fields `x` and `y`. The input has `x1 y1 x2 y2`. Print `dx: D` and `dy: E` (second minus first) and `manhattan: M`, the sum of the absolute values of dx and dy.

**Example**

Input (also in `in.txt`):
```
1 2 4 6
```
Output:
```
dx: 3
dy: 4
manhattan: 7
```

**Focus:** a record (a struct) gives a group of values one name and one type, with a name for each part. `abs` gives the absolute value (in C it comes from `<stdlib.h>`, in C++ from `<cstdlib>`, in Rust it is `.abs()`).
