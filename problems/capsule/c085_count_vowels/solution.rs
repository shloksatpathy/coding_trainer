use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let line = input.lines().next().unwrap();
    let mut count = 0;
    for ch in line.chars() {
        let ch = ch.to_ascii_lowercase();
        if ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' {
            count += 1;
        }
    }
    println!("{}", count);
}
