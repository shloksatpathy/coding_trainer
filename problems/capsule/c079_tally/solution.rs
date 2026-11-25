use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let mut count = vec![0; 10];
    for i in 0..n {
        count[a[i] as usize] += 1;
    }
    for v in 0..10 {
        if count[v] > 0 {
            println!("{}: {}", v, count[v]);
        }
    }
}
