# C070 · Checkpoint: primes in a range

Write `is_prime(n)`: true when n ≥ 2 and no number from 2 up to the square root of n divides it (loop while `i * i <= n`). Read `a b` (0 ≤ a ≤ b ≤ 1 000 100) and print the primes from `a` to `b` on one line, separated by spaces, or `none` if there are none.

**Example**

Input (also in `in.txt`):
```
1 20
```
Output:
```
2 3 5 7 11 13 17 19
```

**Focus:** checkpoint for module 7: a yes/no function with an early return, used by a loop in the main program.
