use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let k: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let mut window = 0;
    for i in 0..k {
        window += a[i];
    }
    print!("{:.2}", window as f64 / k as f64);
    for i in k..n {
        window += a[i] - a[i - k];
        print!(" {:.2}", window as f64 / k as f64);
    }
    println!();
}
