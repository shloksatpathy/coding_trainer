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
    let m: usize = words.next().unwrap().parse().unwrap();
    let mut b: Vec<i64> = Vec::new();
    for _ in 0..m {
        b.push(words.next().unwrap().parse().unwrap());
    }
    let mut i = 0;
    let mut j = 0;
    let mut out = String::new();
    for k in 0..n + m {
        if k > 0 {
            out.push(' ');
        }
        if j == m || (i < n && a[i] <= b[j]) {
            out.push_str(&a[i].to_string());
            i += 1;
        } else {
            out.push_str(&b[j].to_string());
            j += 1;
        }
    }
    println!("{}", out);
}
