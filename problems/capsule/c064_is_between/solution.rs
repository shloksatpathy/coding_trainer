use std::io::Read;

fn is_between(x: i64, lo: i64, hi: i64) -> bool {
    lo <= x && x <= hi
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let lo: i64 = words.next().unwrap().parse().unwrap();
    let hi: i64 = words.next().unwrap().parse().unwrap();
    let n: i64 = words.next().unwrap().parse().unwrap();
    for _ in 0..n {
        let x: i64 = words.next().unwrap().parse().unwrap();
        if is_between(x, lo, hi) {
            println!("yes");
        } else {
            println!("no");
        }
    }
}
