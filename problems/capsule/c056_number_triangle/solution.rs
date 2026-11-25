use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    for i in 1..=n {
        for j in 1..=i {
            if j > 1 {
                print!(" ");
            }
            print!("{}", j);
        }
        println!();
    }
}
