**Learn · a loop inside a loop**

The inner loop runs all its rounds for each round of the outer loop.

```rust
for row in 1..=2 {
    for col in 1..=3 {
        print!("{}{} ", row, col);
    }
    println!();
}
```

prints `11 12 13` on the first line and `21 22 23` on the second.
