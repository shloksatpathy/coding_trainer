use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let w: i64 = words.next().unwrap().parse().unwrap();
    let h: i64 = words.next().unwrap().parse().unwrap();
    for _ in 0..h {
        for _ in 0..w {
            print!("#");
        }
        println!();
    }
}
