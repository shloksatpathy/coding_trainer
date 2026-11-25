**Learn · splitting a line at commas**

`line.split(',')` gives the pieces between commas one by one.

```rust
let mut parts = "ann,oslo".split(',');
let name = parts.next().unwrap();
let city = parts.next().unwrap();
println!("{} {}", name, city);
```
