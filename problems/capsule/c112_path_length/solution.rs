use std::io::Read;

struct Point {
    x: i64,
    y: i64,
}

fn distance(p: &Point, q: &Point) -> f64 {
    let dx = (q.x - p.x) as f64;
    let dy = (q.y - p.y) as f64;
    (dx * dx + dy * dy).sqrt()
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut next = || -> i64 { words.next().unwrap().parse().unwrap() };
    let n = next() as usize;
    let mut pts: Vec<Point> = Vec::new();
    for _ in 0..n {
        pts.push(Point { x: next(), y: next() });
    }
    let mut total = 0.0;
    for i in 1..n {
        total += distance(&pts[i - 1], &pts[i]);
    }
    println!("{:.2}", total);
}
