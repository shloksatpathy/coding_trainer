# P09 · Fibonacci and overflow

Read `n` (1 ≤ n ≤ 94). Print the first `n` Fibonacci numbers (F0 = 0, F1 = 1) on one line. On the second line, print the largest k where F(k) fits in an unsigned 64-bit integer — compute it, don't hard-code it.

**Focus:** C wraps unsigned overflow silently, Rust panics in debug builds, and Python never overflows. In Rust, detect the limit with `checked_add` returning `None`.

**Sample input** (also in `in.txt`):
```
10
```
