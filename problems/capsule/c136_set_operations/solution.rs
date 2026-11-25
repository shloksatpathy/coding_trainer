use std::io::Read;

use std::collections::BTreeSet;

fn read_set(line: &str) -> BTreeSet<i64> {
    line.split_whitespace().skip(1).map(|w| w.parse().unwrap()).collect()
}

fn show(label: &str, s: BTreeSet<i64>) {
    print!("{}:", label);
    if s.is_empty() {
        print!(" none");
    }
    for x in &s {
        print!(" {}", x);
    }
    println!();
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let a = read_set(lines.next().unwrap());
    let b = read_set(lines.next().unwrap());
    show("union", a.union(&b).cloned().collect());
    show("both", a.intersection(&b).cloned().collect());
    show("only first", a.difference(&b).cloned().collect());
}
