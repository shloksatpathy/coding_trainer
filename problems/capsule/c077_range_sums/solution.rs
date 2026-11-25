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
    let mut p: Vec<i64> = vec![0; n + 1];
    for i in 1..=n {
        p[i] = p[i - 1] + a[i - 1];
    }
    let q: usize = words.next().unwrap().parse().unwrap();
    for _ in 0..q {
        let l: usize = words.next().unwrap().parse().unwrap();
        let r: usize = words.next().unwrap().parse().unwrap();
        println!("{}", p[r] - p[l - 1]);
    }
}
