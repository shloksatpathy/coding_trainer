# P08 · GCD and LCM

Read `a b` (positive). Print `gcd lcm` using Euclid's algorithm. Write gcd both iteratively and recursively.

**Focus:** compute LCM as `a / gcd * b`, not `a * b / gcd`. The first form avoids overflow for large inputs (use 64-bit integers).

**Sample input** (also in `in.txt`):
```
12 18
```
