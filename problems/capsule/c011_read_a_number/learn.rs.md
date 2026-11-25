**Learn · variables and reading a number**

The starting code reads all of the input into the text `input`. `.trim()` drops the line break, `.parse()` turns the text into a number of the type you name (`i64` is a whole number), and `.unwrap()` stops the program if that fails.

```rust
let age: i64 = input.trim().parse().unwrap();
println!("{}", age + 1);
```

With the input `41` this prints `42`.
