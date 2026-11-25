use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let mut total = 0;
    for i in 0..n {
        total += a[i];
        if i > 0 {
            print!(" ");
        }
        print!("{}", total);
    }
    println!();
}
