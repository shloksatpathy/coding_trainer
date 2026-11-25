# C102 · Fibonacci, recursively

Write a recursive `fib(n)`: `fib(0)` is 0, `fib(1)` is 1, and `fib(n)` is `fib(n - 1) + fib(n - 2)`. Read `n` (0 ≤ n ≤ 25) and print `fib(n)`.

**Example**

Input (also in `in.txt`):
```
10
```
Output:
```
55
```

**Focus:** two recursive calls per call. It works, but the same values are computed again and again: try n = 40 and wait. Module 15 shows the fix.
