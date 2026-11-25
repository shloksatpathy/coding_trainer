**Learn · leaving a loop with break**

`loop { ... }` loops forever; `break` leaves the loop right away.

```rust
let mut words = input.split_whitespace();
loop {
    let x: i64 = words.next().unwrap().parse().unwrap();
    if x < 0 {
        break;
    }
    println!("{}", x * 2);
}
```

doubles numbers until the first negative one.
