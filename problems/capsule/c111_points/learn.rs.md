**Learn · records**

`struct Point { ... }` defines a new type made of named fields; `Point { x: 3, y: 4 }` creates one and `p.x` is a field. The solutions here use a small helper `next()` that parses the next word; see the reference solution.

```rust
struct Point {
    x: i64,
    y: i64,
}

fn main() {
    let p = Point { x: 3, y: 4 };
    println!("{}", p.x + p.y);
}
```

prints `7`.
