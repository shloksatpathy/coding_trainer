**Learn · reading many values**

Keep taking words from the same `split_whitespace()`; it skips line breaks too. `for _ in 0..n` repeats n times when the counter isn't needed.

```rust
let mut words = input.split_whitespace();
let n: i64 = words.next().unwrap().parse().unwrap();
let mut total = 0;
for _ in 0..n {
    let x: i64 = words.next().unwrap().parse().unwrap();
    total += x;
}
println!("{}", total);
```

With the input `3` and `4 5 6` this prints the sum, `15`.
