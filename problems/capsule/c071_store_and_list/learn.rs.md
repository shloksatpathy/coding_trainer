**Learn · arrays and lists**

`Vec<i64>` is a growable list: `Vec::new()` makes an empty one, `.push(x)` adds `x` at the end, `a[i]` is the value at position `i` (counting from 0; `i` must be a `usize`) and `a.len()` is the count.

```rust
let mut words = input.split_whitespace();
let n: usize = words.next().unwrap().parse().unwrap();
let mut a: Vec<i64> = Vec::new();
for _ in 0..n {
    a.push(words.next().unwrap().parse().unwrap());
}
println!("{} {}", a[0], a.len());
```

With the input `3` and `7 8 9` this prints `7 3`.
