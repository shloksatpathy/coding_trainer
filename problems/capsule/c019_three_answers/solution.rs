use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let name = words.next().unwrap();
    let city = words.next().unwrap();
    let year: i64 = words.next().unwrap().parse().unwrap();
    println!("{} from {}, since {}", name, city, year);
    println!("That is {} years before 2026.", 2026 - year);
}
