use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let s: i64 = input.trim().parse().unwrap();
    println!("{}:{:02}:{:02}", s / 3600, s / 60 % 60, s % 60);
}
