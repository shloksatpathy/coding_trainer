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
    let mut first = a[0];
    for i in 0..n {
        if a[i] > first {
            first = a[i];
        }
    }
    let mut found = false;
    let mut second = 0;
    for i in 0..n {
        if a[i] < first && (!found || a[i] > second) {
            second = a[i];
            found = true;
        }
    }
    if found {
        println!("{}", second);
    } else {
        println!("none");
    }
}
