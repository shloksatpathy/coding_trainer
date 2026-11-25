**Learn · decimal to whole number**

`x.floor()`, `x.ceil()` and `x.trunc()` round down, round up and cut off the fraction; they still give an `f64`. `as i64` converts to a whole number.

```rust
let x: f64 = -3.5;
println!("{} {} {}", x.floor() as i64, x.ceil() as i64, x.trunc() as i64);
```

prints `-4 -3 -3`.
