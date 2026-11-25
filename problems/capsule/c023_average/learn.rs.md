**Learn · decimal numbers**

`f64` is a decimal number. Rust never mixes whole and decimal numbers by itself: convert with `as f64` first. `{:.2}` prints 2 decimals.

```rust
let half = 7 as f64 / 2.0;
println!("{:.2}", half);
```

prints `3.50`.
