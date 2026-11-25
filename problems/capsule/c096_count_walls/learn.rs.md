**Learn · a grid of characters**

Keep each row as bytes: `g.push(words.next().unwrap().as_bytes())`. Then `g[i][j]` is a `u8`; compare it with `b'#'`.

```rust
let g = vec!["#.".as_bytes(), ".#".as_bytes()];
println!("{}", g[1][1] == b'#');
```

prints that the bottom-right character is a wall.
