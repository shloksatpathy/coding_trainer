# P44 · Word frequency

Read a line of lowercase words separated by spaces. Print each distinct word and its count as `word count`, sorted by count (highest first), then alphabetically.

**Focus:** count with a hash map, then sort the (word, count) pairs with a two-key comparator. C: an array of structs with linear search is fine here. **Rust:** `HashMap<&str, usize>` borrowing from the input line, `entry(w).or_insert(0)`, then `sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(b.0)))`.

**Sample input** (also in `in.txt`):
```
the cat and the hat and the bat
```
