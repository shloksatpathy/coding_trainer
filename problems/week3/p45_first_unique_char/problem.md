# P45 · First unique character

Read a word of lowercase letters. Print the index of its first character that appears exactly once, or `-1`.

Samples: `leetcode` → `0` · `loveleetcode` → `2` · `aabb` → `-1`

**Focus:** two passes over a 26-slot count array (a tiny hash table). Compare with a `HashMap<char, usize>` version in Rust.

**Sample input** (also in `in.txt`):
```
leetcode
```
