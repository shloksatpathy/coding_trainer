use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut x: i64 = input.trim().parse().unwrap();
    println!("start: {}", x);
    x += 5;
    println!("+5: {}", x);
    x *= 2;
    println!("*2: {}", x);
    x -= 3;
    println!("-3: {}", x);
}
