use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let t: i64 = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let mut found = 0;
    if n > 1 {
        let mut i = 0;
        let mut j = n - 1;
        while i < j {
            let s = a[i] + a[j];
            if s == t {
                println!("{} {}", a[i], a[j]);
                found += 1;
                i += 1;
                j -= 1;
            } else if s < t {
                i += 1;
            } else {
                j -= 1;
            }
        }
    }
    if found == 0 {
        println!("none");
    }
}
