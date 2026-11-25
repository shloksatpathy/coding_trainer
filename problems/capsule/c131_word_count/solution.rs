use std::io::Read;

use std::collections::HashMap;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut count: HashMap<&str, i64> = HashMap::new();
    let mut order: Vec<&str> = Vec::new();
    for w in input.split_whitespace().skip(1) {
        if !count.contains_key(w) {
            order.push(w);
        }
        *count.entry(w).or_insert(0) += 1;
    }
    for w in &order {
        println!("{}: {}", w, count[w]);
    }
}
