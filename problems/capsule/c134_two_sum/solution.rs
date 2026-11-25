use std::io::Read;

use std::collections::HashMap;

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
    let mut first: HashMap<i64, usize> = HashMap::new();
    for j in 0..n {
        if let Some(i) = first.get(&(t - a[j])) {
            println!("{} {}", i + 1, j + 1);
            return;
        }
        first.entry(a[j]).or_insert(j);
    }
    println!("none");
}
