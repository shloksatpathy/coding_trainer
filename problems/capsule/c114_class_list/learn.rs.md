**Learn · an array of records**

A `Vec` can hold records: `s[i].score`. A text field has the type `String`; `.to_string()` makes a `String` from a word. `Student { name, score }` fills fields from variables with the same names.

```rust
let s = vec![
    Student { name: "ann".to_string(), score: 90 },
    Student { name: "bob".to_string(), score: 72 },
];
println!("{}", s[1].name);
```

prints `bob`.
