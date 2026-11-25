**Learn · fast lookups: hashing**

`HashSet` and `HashMap` are hash tables: a key's hash says where to store it, so a lookup costs about one step however many keys there are.

```rust
let mut seen: HashSet<i64> = HashSet::new();
for x in [4, 8, 4] {
    println!("{}", seen.contains(&x));
    seen.insert(x);
}
```

prints no, no, yes (as false/true or 0/1).
