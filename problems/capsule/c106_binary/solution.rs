use std::io::Read;

fn binary(n: i64) {
    if n >= 2 {
        binary(n / 2);
    }
    print!("{}", n % 2);
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    binary(n);
    println!();
}
