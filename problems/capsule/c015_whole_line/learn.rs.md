**Learn · reading a whole line**

`input.lines()` splits the input into lines; `.next()` takes the first one, without its line break.

```rust
let line = input.lines().next().unwrap();
println!("[{}]", line);
```
