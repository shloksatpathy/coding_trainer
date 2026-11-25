use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let name = input.trim();
    println!("Hello, {}!", name);
}
