# C112 · Path length

The first line has `n` (1 ≤ n ≤ 1000); each of the next `n` lines has a point `x y`. Write `distance(p, q)` taking two `Point`s and returning the straight-line distance √(dx² + dy²). Print the length of the path that visits the points in order, with 2 decimals.

**Example**

Input (also in `in.txt`):
```
3
0 0
3 4
3 0
```
Output:
```
9.00
```

**Focus:** passing records to functions; a square root comes from `math.sqrt` (Python), `sqrt` in `<math.h>` (C), `std::sqrt` in `<cmath>` (C++) or `.sqrt()` on an `f64` (Rust).
