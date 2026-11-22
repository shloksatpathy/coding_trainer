# P10 · Factorial

Read `n` (0 ≤ n ≤ 20). Compute n! both iteratively and recursively and print both on one line: `iterative recursive`.

Samples: `5` → `120 120` · `20` → `2432902008176640000 2432902008176640000`

**Analysis:** 20! is the largest factorial that fits in 64 bits, and 21! overflows. Python has arbitrary-precision integers, so it has no limit. Note this in a comment.

**Sample input** (also in `in.txt`):
```
5
```
