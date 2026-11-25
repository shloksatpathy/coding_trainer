**Learn · big whole numbers**

`i32` holds values up to 2 147 483 647 and `i64` up to about 9.2 × 10^18. Past the limit the program stops with a panic, or (in an optimized build, like the checker's) silently wraps around to wrong values.

```rust
let big: i64 = 1_000_000_000 * 1_000_000_000;
println!("{}", big);
```

prints `1000000000000000000`.
