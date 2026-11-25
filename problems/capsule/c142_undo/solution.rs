use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut words: Vec<&str> = Vec::new();
    for _ in 0..n {
        let cmd = tokens.next().unwrap();
        if cmd == "add" {
            words.push(tokens.next().unwrap());
        } else if cmd == "undo" {
            words.pop();
        } else if words.is_empty() {
            println!("(empty)");
        } else {
            println!("{}", words.join(" "));
        }
    }
}
