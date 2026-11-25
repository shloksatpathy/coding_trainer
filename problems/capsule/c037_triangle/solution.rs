use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();
    let c: i64 = words.next().unwrap().parse().unwrap();
    if a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a {
        println!("not a triangle");
    } else if a == b && b == c {
        println!("equilateral");
    } else if a == b || b == c || a == c {
        println!("isosceles");
    } else {
        println!("scalene");
    }
}
