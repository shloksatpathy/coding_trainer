use std::io::Read;

struct Item {
    id: String,
    qty: i64,
}

fn find(items: &Vec<Item>, key: &str) -> i64 {
    for i in 0..items.len() {
        if items[i].id == key {
            return i as i64;
        }
    }
    -1
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut items: Vec<Item> = Vec::new();
    for _ in 0..n {
        let id = words.next().unwrap().to_string();
        let qty: i64 = words.next().unwrap().parse().unwrap();
        items.push(Item { id, qty });
    }
    let m: usize = words.next().unwrap().parse().unwrap();
    for _ in 0..m {
        let key = words.next().unwrap();
        let change: i64 = words.next().unwrap().parse().unwrap();
        let k = find(&items, key);
        if k == -1 {
            println!("unknown {}", key);
        } else {
            items[k as usize].qty += change;
        }
    }
    for it in &items {
        println!("{}: {}", it.id, it.qty);
    }
}
