use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let d: i64 = input.trim().parse().unwrap();
    if d == 6 || d == 7 {
        println!("weekend");
    } else if d >= 1 && d <= 5 {
        println!("weekday");
    } else {
        println!("invalid");
    }
}
