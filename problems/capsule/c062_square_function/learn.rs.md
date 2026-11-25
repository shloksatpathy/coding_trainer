**Learn · returning a value**

`-> i64` gives the type of the returned value. The last expression of the body, written without `;`, is the value returned (`return value;` also works).

```rust
fn double(x: i64) -> i64 {
    x * 2
}

fn main() {
    let y = double(5) + 1;
    println!("{}", y);
}
```

prints `11`.
