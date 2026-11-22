# P11 · Fast power (modular exponentiation)

Read `x n m` (0 ≤ x, 0 ≤ n ≤ 10^18, 1 ≤ m ≤ 10^9). Print `x^n mod m` using binary exponentiation.

**Analysis:** the naive loop does n multiplications, binary exponentiation does about log₂(n). Try n = 10^18 and see which one finishes. Keep values below m before multiplying so the product fits in 64 bits.

**Sample input** (also in `in.txt`):
```
2 10 1000
```
