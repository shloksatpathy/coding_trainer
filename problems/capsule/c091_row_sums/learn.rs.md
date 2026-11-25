**Learn · grids**

A `Vec<Vec<i64>>` is a list of rows: build each row as a `Vec` and push it. `g[i][j]` is row `i`, column `j`, both counting from 0. `.parse::<i64>()` names the type where Rust can't guess it.

```rust
let g = vec![vec![1, 2, 3], vec![4, 5, 6]];
println!("{}", g[1][0]);
```

prints `4`: row 1, column 0.
