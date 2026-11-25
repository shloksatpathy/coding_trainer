use std::io::Read;

use std::collections::HashMap;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let mut count: HashMap<i64, i64> = HashMap::new();
    for i in 0..n {
        *count.entry(a[i]).or_insert(0) += 1;
    }
    let mut best = a[0];
    let mut best_count = 0;
    for (&x, &k) in &count {
        if k > best_count || (k == best_count && x < best) {
            best = x;
            best_count = k;
        }
    }
    println!("value: {}", best);
    println!("count: {}", best_count);
    println!("distinct: {}", count.len());
}
