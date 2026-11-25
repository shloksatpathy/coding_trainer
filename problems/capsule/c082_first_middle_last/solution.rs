use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let w = input.trim();
    let b = w.as_bytes();
    let n = b.len();
    println!("first: {}", b[0] as char);
    println!("middle: {}", b[n / 2] as char);
    println!("last: {}", b[n - 1] as char);
}
