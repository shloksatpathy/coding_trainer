**Learn · an array filled with zeros**

`vec![0; 10]` is a `Vec` of ten zeros. A value used as an index must be converted with `as usize`.

```rust
let mut seen = vec![0; 3];
seen[2] += 1;
println!("{} {} {}", seen[0], seen[1], seen[2]);
```
