use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    println!("{}", n / 1000 + n / 100 % 10 + n / 10 % 10 + n % 10);
}
