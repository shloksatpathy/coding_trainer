**Learn · maps**

`HashMap` (from `std::collections`) maps keys to values: `*m.entry(key).or_insert(0) += 1` adds 1, starting from 0; `m.contains_key(key)` checks; `m[key]` reads. It doesn't keep any order, so remember the first-seen order separately.

```rust
let mut age: HashMap<&str, i64> = HashMap::new();
age.insert("ann", 30);
println!("{} {}", age.contains_key("ann"), age.contains_key("bob"));
```
