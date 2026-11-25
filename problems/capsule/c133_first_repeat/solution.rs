use std::io::Read;

use std::collections::HashSet;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let mut seen: HashSet<i64> = HashSet::new();
    for i in 0..n {
        if !seen.insert(a[i]) {
            println!("{}", a[i]);
            return;
        }
    }
    println!("none");
}
