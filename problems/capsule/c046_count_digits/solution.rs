use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut n: i64 = input.trim().parse().unwrap();
    let mut digits = 1;
    while n >= 10 {
        n /= 10;
        digits += 1;
    }
    println!("{}", digits);
}
