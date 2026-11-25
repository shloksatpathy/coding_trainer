**Learn · reading decimal numbers**

Parse into `f64`. Decimal literals need a point: write `2.0`, not `2`, next to an `f64`.

```rust
let price: f64 = input.trim().parse().unwrap();
println!("{:.2}", price * 2.0);
```

With the input `1.25` this prints `2.50`.
