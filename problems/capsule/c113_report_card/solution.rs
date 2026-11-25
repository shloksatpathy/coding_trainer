use std::io::Read;

struct Report {
    name: String,
    scores: [i64; 3],
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let name = words.next().unwrap().to_string();
    let mut scores: [i64; 3] = [0; 3];
    for i in 0..3 {
        scores[i] = words.next().unwrap().parse().unwrap();
    }
    let r = Report { name, scores };
    let mut total = 0;
    let mut best = r.scores[0];
    for i in 0..3 {
        total += r.scores[i];
        if r.scores[i] > best {
            best = r.scores[i];
        }
    }
    println!("{}: total {}, average {:.2}, best {}", r.name, total, total as f64 / 3.0, best);
}
