use std::io::Read;

fn count(a: &Vec<i64>, i: usize, left: i64) -> i64 {
    if i == a.len() {
        if left == 0 {
            return 1;
        }
        return 0;
    }
    count(a, i + 1, left) + count(a, i + 1, left - a[i])
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let t: i64 = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    println!("{}", count(&a, 0, t));
}
