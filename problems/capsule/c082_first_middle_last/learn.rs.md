**Learn · one character**

Rust text can't be indexed directly. `text.as_bytes()` gives its bytes; `b[i] as char` is the character at index `i` (for plain English text).

```rust
let name = "Ada";
let b = name.as_bytes();
println!("{}", b[1] as char);
```

prints `d`.
