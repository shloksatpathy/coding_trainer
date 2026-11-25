**Learn · more than two cases**

`else if` adds another condition, checked only when the ones before it were false.

```rust
if t < 10 {
    println!("cold");
} else if t < 25 {
    println!("mild");
} else {
    println!("hot");
}
```
