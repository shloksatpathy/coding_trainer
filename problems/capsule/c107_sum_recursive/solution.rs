use std::io::Read;

fn total(a: &Vec<i64>, i: usize) -> i64 {
    if i == a.len() {
        return 0;
    }
    a[i] + total(a, i + 1)
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    println!("{}", total(&a, 0));
}
