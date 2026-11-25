**Learn · updating a variable**

`x += 5` is short for `x = x + 5`. The same works with `-=`, `*=` and `/=`.

```rust
let mut score = 10;
score += 5;
score *= 2;
println!("{}", score);
```

prints `30`.
