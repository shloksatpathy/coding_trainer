**Learn · looking at each character**

`for ch in text.chars()` goes through the characters. `ch.is_ascii_uppercase()` and `ch.is_ascii_digit()` test one; `ch.to_ascii_lowercase()` converts it.

```rust
for ch in "a1B".chars() {
    if ch.is_ascii_uppercase() {
        println!("{} is uppercase", ch);
    }
}
```

prints `B is uppercase`.
