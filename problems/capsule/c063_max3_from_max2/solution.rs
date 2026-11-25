use std::io::Read;

fn max2(a: i64, b: i64) -> i64 {
    if a > b {
        a
    } else {
        b
    }
}

fn max3(a: i64, b: i64, c: i64) -> i64 {
    max2(max2(a, b), c)
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();
    let c: i64 = words.next().unwrap().parse().unwrap();
    println!("{}", max3(a, b, c));
}
