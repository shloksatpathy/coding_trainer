# P07 · Primes up to n (Sieve of Eratosthenes)

Read `n` (n ≥ 2). Print all primes ≤ n on one line, separated by spaces, using a sieve.

**Analysis:** the sieve is O(n log log n), while trial division of each number is O(n√n). Run both for n = 1,000,000 in C and Python and note the time difference.

**Sample input** (also in `in.txt`):
```
30
```
