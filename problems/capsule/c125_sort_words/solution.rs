use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words: Vec<&str> = input.split_whitespace().skip(1).collect();
    words.sort_by(|a, b| a.len().cmp(&b.len()).then(a.cmp(b)));
    for w in &words {
        println!("{}", w);
    }
}
