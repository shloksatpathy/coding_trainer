use std::io::Read;

fn digit_sum(n: i64) -> i64 {
    if n < 10 {
        return n;
    }
    n % 10 + digit_sum(n / 10)
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    println!("{}", digit_sum(n));
}
