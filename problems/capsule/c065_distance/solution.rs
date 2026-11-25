use std::io::Read;

fn absolute(x: i64) -> i64 {
    if x < 0 {
        -x
    } else {
        x
    }
}

fn distance(a: i64, b: i64) -> i64 {
    absolute(a - b)
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: i64 = words.next().unwrap().parse().unwrap();
    for _ in 0..n {
        let a: i64 = words.next().unwrap().parse().unwrap();
        let b: i64 = words.next().unwrap().parse().unwrap();
        println!("{}", distance(a, b));
    }
}
