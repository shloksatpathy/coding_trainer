use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut count = 0;
    let mut total = 0;
    let mut longest = "";
    let mut shortest = "";
    for w in input.split_whitespace() {
        if count == 0 || w.len() > longest.len() {
            longest = w;
        }
        if count == 0 || w.len() < shortest.len() {
            shortest = w;
        }
        total += w.len();
        count += 1;
    }
    println!("words: {}", count);
    println!("longest: {}", longest);
    println!("shortest: {}", shortest);
    println!("average: {:.2}", total as f64 / count as f64);
}
