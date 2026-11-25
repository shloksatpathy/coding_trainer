use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    let mut total: i64 = 0;
    for i in 1..=n {
        total += i;
    }
    println!("{}", total);
}
