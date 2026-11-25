use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let x: f64 = input.trim().parse().unwrap();
    println!("{} {} {}", x.floor() as i64, x.ceil() as i64, x.trunc() as i64);
}
