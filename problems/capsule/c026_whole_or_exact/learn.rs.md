**Learn · converting a whole number to a decimal**

`as f64` converts a whole number: `n as f64 / 2.0` is decimal division.

```rust
let n: i64 = 7;
println!("{} {}", n / 2, n as f64 / 2.0);
```

prints `3 3.5`.
