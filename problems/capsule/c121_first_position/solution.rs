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
    let q: usize = words.next().unwrap().parse().unwrap();
    for _ in 0..q {
        let x: i64 = words.next().unwrap().parse().unwrap();
        let mut pos: i64 = -1;
        for i in 0..n {
            if a[i] == x {
                pos = i as i64 + 1;
                break;
            }
        }
        println!("{}", pos);
    }
}
