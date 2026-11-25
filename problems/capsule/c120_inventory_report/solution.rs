use std::io::Read;

struct Line {
    name: String,
    total: i64,
    qty: i64,
}

fn money(cents: i64) -> String {
    format!("{}.{:02}", cents / 100, cents % 100)
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut lines: Vec<Line> = Vec::new();
    let mut grand = 0;
    for _ in 0..n {
        let name = words.next().unwrap().to_string();
        let price: i64 = words.next().unwrap().parse().unwrap();
        let qty: i64 = words.next().unwrap().parse().unwrap();
        lines.push(Line { name, total: price * qty, qty });
        grand += price * qty;
    }
    lines.sort_by(|a, b| b.total.cmp(&a.total).then(a.name.cmp(&b.name)));
    for x in &lines {
        println!("{:<10}{:>5}{:>10}", x.name, x.qty, money(x.total));
    }
    println!("{:<15}{:>10}", "TOTAL", money(grand));
}
