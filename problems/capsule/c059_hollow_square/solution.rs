use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    for r in 0..n {
        for col in 0..n {
            if r == 0 || r == n - 1 || col == 0 || col == n - 1 {
                print!("#");
            } else {
                print!(" ");
            }
        }
        println!();
    }
}
