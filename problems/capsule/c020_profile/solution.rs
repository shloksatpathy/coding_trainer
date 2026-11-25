use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    const THIS_YEAR: i64 = 2026;
    let mut words = input.split_whitespace();
    let name = words.next().unwrap();
    let age: i64 = words.next().unwrap().parse().unwrap();
    let born = THIS_YEAR - age;
    println!("Hello, {}! You are {}.", name, age);
    println!("In 10 years you will be {}.", age + 10);
    println!("You were born in {} or {}.", born, born - 1);
}
