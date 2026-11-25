use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    for r in 1..=n {
        for col in 1..=n {
            print!("{:4}", r * col);
        }
        println!();
    }
}
