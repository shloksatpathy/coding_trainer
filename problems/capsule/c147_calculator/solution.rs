use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut total: i64 = 0;
    let mut term: i64 = tokens.next().unwrap().parse().unwrap();
    while let Some(op) = tokens.next() {
        let x: i64 = tokens.next().unwrap().parse().unwrap();
        if op == "*" {
            term *= x;
        } else {
            total += term;
            if op == "+" {
                term = x;
            } else {
                term = -x;
            }
        }
    }
    println!("{}", total + term);
}
