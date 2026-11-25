**Learn · recursion**

A function may call itself. Each call works on a smaller problem, and a base case answers the smallest problem directly so that the calls stop.

```rust
fn countdown(n: i64) {
    if n == 0 {
        println!("go!");
        return;
    }
    println!("{}", n);
    countdown(n - 1);
}
```

`countdown(3)` prints `3`, `2`, `1` and `go!`.
