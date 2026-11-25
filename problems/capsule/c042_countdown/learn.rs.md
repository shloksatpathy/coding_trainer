**Learn · while loops**

`while condition { ... }` checks the condition before every round and stops as soon as it is false.

```rust
let mut x = 1;
while x < 100 {
    x *= 3;
}
println!("{}", x);
```

prints `243`, the first power of 3 that is 100 or more.
