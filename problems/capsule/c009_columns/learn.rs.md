**Learn · fixed widths**

`{:<8}` pads the value to 8 characters, aligned left; `{:>4}` aligns right.

```rust
println!("{:<8}|{:>4}|", "pear", 7);
```

prints `pear    |   7|`.
