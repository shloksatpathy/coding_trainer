use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let total: i64 = words.next().unwrap().parse().unwrap();
    let count: i64 = words.next().unwrap().parse().unwrap();
    println!("whole: {}", total / count);
    println!("exact: {:.3}", total as f64 / count as f64);
}
