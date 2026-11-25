use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let x: i64 = words.next().unwrap().parse().unwrap();
    let y: i64 = words.next().unwrap().parse().unwrap();
    if x == 0 && y == 0 {
        println!("origin");
    } else if y == 0 {
        println!("x-axis");
    } else if x == 0 {
        println!("y-axis");
    } else if x > 0 {
        if y > 0 {
            println!("Q1");
        } else {
            println!("Q4");
        }
    } else {
        if y > 0 {
            println!("Q2");
        } else {
            println!("Q3");
        }
    }
}
