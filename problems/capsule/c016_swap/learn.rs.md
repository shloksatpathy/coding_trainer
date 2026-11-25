**Learn · changing a variable**

Rust variables can't change unless they are declared with `let mut`.

```rust
let mut x = 1;
x = 7;
println!("{}", x);
```

prints `7`: the old value is gone.
