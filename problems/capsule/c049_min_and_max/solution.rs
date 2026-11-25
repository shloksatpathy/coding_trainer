use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: i64 = words.next().unwrap().parse().unwrap();
    let first: i64 = words.next().unwrap().parse().unwrap();
    let mut lo = first;
    let mut hi = first;
    for _ in 1..n {
        let x: i64 = words.next().unwrap().parse().unwrap();
        if x < lo {
            lo = x;
        }
        if x > hi {
            hi = x;
        }
    }
    println!("min: {}", lo);
    println!("max: {}", hi);
}
