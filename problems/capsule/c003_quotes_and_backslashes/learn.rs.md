**Learn · escapes**

A `"` would end the text, so inside quotes you write `\"` for a quote. A `\` starts an escape (like `\n`), so you write `\\` for one backslash.

```rust
println!("A \"quoted\" word");
println!("one\\two");
```

prints `A "quoted" word` and `one\two`.
