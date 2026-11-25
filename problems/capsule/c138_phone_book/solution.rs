use std::io::Read;

use std::collections::HashMap;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut book: HashMap<&str, &str> = HashMap::new();
    for _ in 0..n {
        let name = words.next().unwrap();
        let number = words.next().unwrap();
        book.insert(name, number);
    }
    let q: usize = words.next().unwrap().parse().unwrap();
    for _ in 0..q {
        let name = words.next().unwrap();
        match book.get(name) {
            Some(number) => println!("{}: {}", name, number),
            None => println!("{}: not found", name),
        }
    }
}
