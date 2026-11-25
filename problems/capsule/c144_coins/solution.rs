use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut amount: i64 = input.trim().parse().unwrap();
    let mut total = 0;
    for coin in [200, 100, 50, 20, 10, 5, 2, 1] {
        let k = amount / coin;
        if k > 0 {
            println!("{} x {}", coin, k);
            amount -= k * coin;
            total += k;
        }
    }
    println!("coins: {}", total);
}
