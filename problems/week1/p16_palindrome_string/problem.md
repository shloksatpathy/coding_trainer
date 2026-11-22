# P16 · Palindrome string

Read a line. Print `true` if it is a palindrome when you ignore case and all non-alphanumeric characters, else `false`.

Samples: `A man, a plan, a canal: Panama` → `true` · `race a car` → `false`

**Focus:** C uses `isalnum` and `tolower` on a `char` array. Rust uses `is_alphanumeric()` and `to_ascii_lowercase()`. Use two pointers, not a reversed copy.

**Sample input** (also in `in.txt`):
```
A man, a plan, a canal: Panama
```
