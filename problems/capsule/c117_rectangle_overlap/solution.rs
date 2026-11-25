use std::io::Read;

struct Rect {
    x1: i64,
    y1: i64,
    x2: i64,
    y2: i64,
}

fn overlap_area(a: &Rect, b: &Rect) -> i64 {
    let w = a.x2.min(b.x2) - a.x1.max(b.x1);
    let h = a.y2.min(b.y2) - a.y1.max(b.y1);
    if w <= 0 || h <= 0 {
        return 0;
    }
    w * h
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut next = || -> i64 { words.next().unwrap().parse().unwrap() };
    let a = Rect { x1: next(), y1: next(), x2: next(), y2: next() };
    let b = Rect { x1: next(), y1: next(), x2: next(), y2: next() };
    println!("{}", overlap_area(&a, &b));
}
