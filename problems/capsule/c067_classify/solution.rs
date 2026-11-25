use std::io::Read;

fn classify(n: i64) -> &'static str {
    if n < 0 {
        return "negative";
    }
    if n == 0 {
        return "zero";
    }
    if n < 10 {
        return "small";
    }
    if n < 100 {
        return "medium";
    }
    "large"
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: i64 = words.next().unwrap().parse().unwrap();
    for _ in 0..n {
        let x: i64 = words.next().unwrap().parse().unwrap();
        println!("{}", classify(x));
    }
}
