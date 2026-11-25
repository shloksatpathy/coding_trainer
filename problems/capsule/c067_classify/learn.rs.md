**Learn · returning early, returning text**

A `return` ends the function at once, so the checks after it need no `else`. Fixed text written in quotes has the type `&'static str`.

```rust
fn size(n: i64) -> &'static str {
    if n < 10 {
        return "short";
    }
    "long"
}
```
