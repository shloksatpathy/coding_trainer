use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let line = input.lines().next().unwrap();
    let b = line.as_bytes();
    let mut i = b.len();
    while i > 0 {
        i -= 1;
        print!("{}", b[i] as char);
    }
    println!();
}
