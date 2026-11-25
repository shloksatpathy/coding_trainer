use std::io::Read;

fn power(base: i64, exp: i64) -> i64 {
    let mut result = 1;
    for _ in 0..exp {
        result *= base;
    }
    result
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let base: i64 = words.next().unwrap().parse().unwrap();
    let exp: i64 = words.next().unwrap().parse().unwrap();
    println!("{}", power(base, exp));
}
