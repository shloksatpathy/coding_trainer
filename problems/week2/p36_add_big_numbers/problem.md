# P36 · Add big numbers with linked lists

Read two non-negative integers `a b` on one line, each up to 100 digits (too big for any built-in integer type in C, C++ and Rust). Store each number's digits in a linked list, least significant digit first, add them digit by digit with a carry, and print the sum.

Don't use Python's big integers — build the lists, like the other languages.

**Focus:** the carry after the last digit (`999 + 1`). **Rust:** `s.bytes().rev()` gives digits from the end.

**Sample input** (also in `in.txt`):
```
999 1
```
