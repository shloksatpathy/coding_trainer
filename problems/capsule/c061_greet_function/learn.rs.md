**Learn · functions**

`fn name(parameter: type)` is written outside `main`. A text parameter has the type `&str`.

```rust
fn show_double(x: i64) {
    println!("{}", x * 2);
}

fn main() {
    show_double(4);
    show_double(10);
}
```

prints `8` and `20`.
