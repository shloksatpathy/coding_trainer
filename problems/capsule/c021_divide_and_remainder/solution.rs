use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();
    let q = a / b;
    let r = a % b;
    println!("a / b = {}", q);
    println!("a % b = {}", r);
    println!("Q * b + R = {}", q * b + r);
}
