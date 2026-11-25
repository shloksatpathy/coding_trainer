**Learn · stacks**

A `Vec` works as a stack: `push(x)`, `last()`, and `pop()`, which returns `Some(top)` or `None` when empty.

```rust
let mut s = vec![1];
s.push(2);
println!("{:?} {:?}", s.pop(), s.pop());
```

The last value pushed comes off first.
