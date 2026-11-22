# P01 · Integer arithmetic

Read two integers `a b` (b ≠ 0). Print `a+b a-b a*b a/b a%b` on one line.

Division and remainder truncate toward zero (the C/C++/Rust behaviour).

**Focus:** C, C++ and Rust truncate division toward zero. Python floors it (`-7 // 2 = -4`, `-7 % 2 = 1`). Make the Python output match the others, and write a comment explaining why the results differ.

**Sample input** (also in `in.txt`):
```
-7 2
```
