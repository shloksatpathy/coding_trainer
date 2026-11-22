# P06 · Reverse number and palindrome

Read a non-negative integer. Print its reverse, a space, then `Palindrome` or `Not palindrome`.

Samples: `12321` → `12321 Palindrome` · `1230` → `321 Not palindrome`

**Focus:** the `% 10` and `/ 10` loop, done arithmetically with no string conversion. In Rust, use `u64` and `let mut`.

**Sample input** (also in `in.txt`):
```
12321
```
