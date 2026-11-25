use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    if n % 2 == 0 {
        println!("even");
    } else {
        println!("odd");
    }
}
