**Learn · for loops**

`for i in 1..=3` runs its block with `i` = 1, 2, 3. `1..3` would stop before 3.

```rust
for i in 1..=3 {
    println!("{}", i * 10);
}
```

prints `10`, `20` and `30` on three lines.
