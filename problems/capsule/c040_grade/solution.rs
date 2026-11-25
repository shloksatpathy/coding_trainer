use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let s: i64 = input.trim().parse().unwrap();
    if s < 0 || s > 100 {
        println!("invalid");
    } else {
        let letter = if s >= 90 {
            'A'
        } else if s >= 80 {
            'B'
        } else if s >= 70 {
            'C'
        } else if s >= 60 {
            'D'
        } else {
            'F'
        };
        if s >= 60 {
            println!("{} pass", letter);
        } else {
            println!("{} fail", letter);
        }
    }
}
