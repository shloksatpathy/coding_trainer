use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    println!("{}", n);
    println!("{}", 2 * n);
    println!("{}", n * n);
}
