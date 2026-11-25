use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut a: i64 = words.next().unwrap().parse().unwrap();
    let mut b: i64 = words.next().unwrap().parse().unwrap();
    println!("before: a={} b={}", a, b);
    let t = a;
    a = b;
    b = t;
    println!("after: a={} b={}", a, b);
}
