use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut count = 0;
    let mut total: i64 = 0;
    loop {
        let x: i64 = words.next().unwrap().parse().unwrap();
        if x == 0 {
            break;
        }
        count += 1;
        total += x;
    }
    println!("count: {}", count);
    println!("sum: {}", total);
}
