use std::io::Read;

fn down_up(n: i64) {
    if n == 0 {
        return;
    }
    println!("{}", n);
    down_up(n - 1);
    println!("{}", n);
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    down_up(n);
}
