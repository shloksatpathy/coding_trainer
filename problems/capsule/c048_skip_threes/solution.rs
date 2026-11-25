use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    let mut first = true;
    for i in 1..=n {
        if i % 3 == 0 {
            continue;
        }
        if !first {
            print!(" ");
        }
        print!("{}", i);
        first = false;
    }
    println!();
}
