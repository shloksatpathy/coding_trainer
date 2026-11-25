use std::io::Read;

struct Point {
    x: i64,
    y: i64,
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut next = || -> i64 { words.next().unwrap().parse().unwrap() };
    let p = Point { x: next(), y: next() };
    let q = Point { x: next(), y: next() };
    let dx = q.x - p.x;
    let dy = q.y - p.y;
    println!("dx: {}", dx);
    println!("dy: {}", dy);
    println!("manhattan: {}", dx.abs() + dy.abs());
}
