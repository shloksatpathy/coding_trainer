**Learn · keeping a copy of a word**

The words from `split_whitespace()` are views into `input`, so a variable of type `&str` can keep one: `best = w`.

```rust
let mut best = "";
for w in input.split_whitespace() {
    best = w;
}
println!("{}", best);
```

keeps the last word.
