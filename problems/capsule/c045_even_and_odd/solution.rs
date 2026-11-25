use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: i64 = words.next().unwrap().parse().unwrap();
    let mut even = 0;
    let mut odd = 0;
    for _ in 0..n {
        let x: i64 = words.next().unwrap().parse().unwrap();
        if x % 2 == 0 {
            even += 1;
        } else {
            odd += 1;
        }
    }
    println!("even: {}", even);
    println!("odd: {}", odd);
}
