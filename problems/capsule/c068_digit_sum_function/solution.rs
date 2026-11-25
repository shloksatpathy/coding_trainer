use std::io::Read;

fn digit_sum(mut n: i64) -> i64 {
    let mut s = 0;
    while n > 0 {
        s += n % 10;
        n /= 10;
    }
    s
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: i64 = words.next().unwrap().parse().unwrap();
    let mut best = -1;
    let mut best_sum = -1;
    for i in 0..n {
        let x: i64 = words.next().unwrap().parse().unwrap();
        if i > 0 {
            print!(" ");
        }
        print!("{}", digit_sum(x));
        if digit_sum(x) > best_sum {
            best_sum = digit_sum(x);
            best = x;
        }
    }
    println!();
    println!("best: {}", best);
}
