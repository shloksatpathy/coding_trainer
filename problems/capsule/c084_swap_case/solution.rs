use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let line = input.lines().next().unwrap();
    for ch in line.chars() {
        if ch.is_ascii_uppercase() {
            print!("{}", ch.to_ascii_lowercase());
        } else if ch.is_ascii_lowercase() {
            print!("{}", ch.to_ascii_uppercase());
        } else {
            print!("{}", ch);
        }
    }
    println!();
}
