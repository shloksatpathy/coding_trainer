**Learn · changing the caller's data**

`&mut Vec<u8>` lends the vector so that the function may change it. Call it with `&mut buf`.

```rust
fn set_first(buf: &mut Vec<u8>) {
    buf[0] = b'x';
}
```
