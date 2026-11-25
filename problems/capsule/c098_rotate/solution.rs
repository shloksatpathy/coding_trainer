use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let r: usize = words.next().unwrap().parse().unwrap();
    let c: usize = words.next().unwrap().parse().unwrap();
    let mut g: Vec<&[u8]> = Vec::new();
    for _ in 0..r {
        g.push(words.next().unwrap().as_bytes());
    }
    for j in 0..c {
        for k in 0..r {
            print!("{}", g[r - 1 - k][j] as char);
        }
        println!();
    }
}
