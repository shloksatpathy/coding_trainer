**Learn · words**

`text.split_whitespace()` splits at any run of spaces and ignores spaces at the ends; `for w in text.split_whitespace()` goes through the words.

```rust
for w in "  to be  ".split_whitespace() {
    println!("{}", w);
}
```

prints `to` and `be` on two lines.
