**Learn · sorted sets and set operations**

`BTreeSet` (from `std::collections`) keeps its values sorted; `a.union(&b)`, `a.intersection(&b)` and `a.difference(&b)` walk the results in order.

```rust
let s: BTreeSet<i64> = vec![3, 1, 3, 2].into_iter().collect();
println!("{:?}", s);
```
