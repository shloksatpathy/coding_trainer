**Learn · reading two numbers**

`.split_whitespace()` cuts the input into words; each `.next()` takes the next word. The variable must be `mut` because taking words changes it.

```rust
let mut words = input.split_whitespace();
let w: i64 = words.next().unwrap().parse().unwrap();
let h: i64 = words.next().unwrap().parse().unwrap();
println!("{}", w * h);
```

With the input `4 5` this prints `20`.
