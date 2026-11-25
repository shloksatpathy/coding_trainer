**Learn · sets**

`HashSet` (from `std::collections`) holds each value at most once; `s.insert(x)` returns true when `x` was new.

```rust
let mut s: HashSet<i64> = HashSet::new();
s.insert(4);
println!("{}", s.insert(4));
```
