use std::io::Read;

fn factorial(n: i64) -> i64 {
    if n == 0 {
        return 1;
    }
    n * factorial(n - 1)
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    println!("{}", factorial(n));
}
