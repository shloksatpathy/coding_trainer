**Learn · sorting with your own rule**

`v.sort_by(|a, b| ...)` sorts with a closure (a small unnamed function) that compares two elements. `x.cmp(&y)` gives the order of two values; `.then(...)` breaks ties with a second comparison. Comparing `b` with `a` reverses the order.

```rust
let mut v = vec![2, 9, 4];
v.sort_by(|a, b| b.cmp(a));
println!("{:?}", v);
```
