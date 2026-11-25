use std::io::Read;

fn greet(name: &str) {
    println!("Hello, {}!", name);
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    for name in input.split_whitespace() {
        greet(name);
    }
}
