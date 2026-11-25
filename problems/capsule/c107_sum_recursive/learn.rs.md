**Learn · passing an array to a function**

`&Vec<i64>` borrows the vector: the function can read it without taking it over. Call it with `&a`.

```rust
fn first(a: &Vec<i64>) -> i64 {
    a[0]
}
```
