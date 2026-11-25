use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut n: i64 = input.trim().parse().unwrap();
    while n > 0 {
        println!("{}", n);
        n -= 1;
    }
    println!("Liftoff!");
}
