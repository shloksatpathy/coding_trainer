**Learn · reading values with separators**

`text.split(':')` splits at every `:` and gives the pieces one by one.

```rust
let mut parts = "09:15".split(':');
let h: i64 = parts.next().unwrap().parse().unwrap();
let m: i64 = parts.next().unwrap().parse().unwrap();
println!("{} {}", h, m);
```

prints `9 15`.
