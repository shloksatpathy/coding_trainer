use std::io::Read;

struct Student {
    name: String,
    score: i64,
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut s: Vec<Student> = Vec::new();
    for _ in 0..n {
        let name = words.next().unwrap().to_string();
        let score: i64 = words.next().unwrap().parse().unwrap();
        s.push(Student { name, score });
    }
    s.sort_by(|a, b| b.score.cmp(&a.score).then(a.name.cmp(&b.name)));
    for i in 0..n {
        println!("{}. {} {}", i + 1, s[i].name, s[i].score);
    }
}
