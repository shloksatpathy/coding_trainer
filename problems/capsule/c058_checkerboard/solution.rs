use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    for r in 0..n {
        for col in 0..n {
            if (r + col) % 2 == 0 {
                print!("#");
            } else {
                print!(".");
            }
        }
        println!();
    }
}
