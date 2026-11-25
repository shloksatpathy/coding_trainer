use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let age: i64 = input.trim().parse().unwrap();
    if age < 3 {
        println!("free");
    } else if age < 13 {
        println!("child 5");
    } else if age < 65 {
        println!("adult 12");
    } else {
        println!("senior 7");
    }
}
