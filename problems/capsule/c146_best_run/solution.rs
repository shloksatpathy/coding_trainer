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
    let mut here = a[0];
    let mut best = a[0];
    for i in 1..n {
        if here > 0 {
            here += a[i];
        } else {
            here = a[i];
        }
        if here > best {
            best = here;
        }
    }
    println!("{}", best);
}
