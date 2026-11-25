use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();
    let c: i64 = words.next().unwrap().parse().unwrap();
    let mut best = a;
    if b > best {
        best = b;
    }
    if c > best {
        best = c;
    }
    println!("{}", best);
}
