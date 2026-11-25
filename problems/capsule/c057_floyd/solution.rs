use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();
    let mut k = 1;
    for i in 1..=n {
        for j in 0..i {
            if j > 0 {
                print!(" ");
            }
            print!("{}", k);
            k += 1;
        }
        println!();
    }
}
