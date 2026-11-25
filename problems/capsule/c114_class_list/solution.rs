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
    let mut top = 0;
    let mut total = 0;
    for i in 0..n {
        total += s[i].score;
        if s[i].score > s[top].score {
            top = i;
        }
    }
    println!("top: {} ({})", s[top].name, s[top].score);
    println!("average: {:.2}", total as f64 / n as f64);
    print!("above:");
    let mut found = 0;
    for i in 0..n {
        if s[i].score * n as i64 > total {
            print!(" {}", s[i].name);
            found += 1;
        }
    }
    if found == 0 {
        print!(" none");
    }
    println!();
}
