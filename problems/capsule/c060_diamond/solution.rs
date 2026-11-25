use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    for k in 1..=2 * n - 1 {
        let i = if k <= n { k } else { 2 * n - k };
        for _ in 0..n - i {
            print!(" ");
        }
        for _ in 0..2 * i - 1 {
            print!("*");
        }
        println!();
    }
}
