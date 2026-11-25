use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let line = lines.next().unwrap();
    let k: u8 = lines.next().unwrap().trim().parse().unwrap();
    for b in line.bytes() {
        if b.is_ascii_lowercase() {
            print!("{}", ((b - b'a' + k) % 26 + b'a') as char);
        } else if b.is_ascii_uppercase() {
            print!("{}", ((b - b'A' + k) % 26 + b'A') as char);
        } else {
            print!("{}", b as char);
        }
    }
    println!();
}
