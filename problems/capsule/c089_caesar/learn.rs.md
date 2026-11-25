**Learn · characters as numbers**

`text.bytes()` gives the character codes as `u8` numbers; `b'a'` is the code of `a`. The letters have consecutive codes, so `b'c' - b'a'` is 2. `code as char` turns a `u8` back into a character.

```rust
println!("{}", (b'a' + 2) as char);
```

prints `c`.
