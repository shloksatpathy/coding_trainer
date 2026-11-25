use std::io::Read;

use std::collections::HashMap;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut group: HashMap<Vec<u8>, usize> = HashMap::new();
    let mut groups: Vec<Vec<&str>> = Vec::new();
    for w in input.split_whitespace().skip(1) {
        let mut key = w.as_bytes().to_vec();
        key.sort();
        if !group.contains_key(&key) {
            group.insert(key.clone(), groups.len());
            groups.push(Vec::new());
        }
        groups[group[&key]].push(w);
    }
    for g in &groups {
        println!("{}", g.join(" "));
    }
}
