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
    let x: i64 = words.next().unwrap().parse().unwrap();
    let mut count = 0;
    for i in 0..n {
        if a[i] == x {
            count += 1;
        }
    }
    println!("count: {}", count);
    print!("positions:");
    for i in 0..n {
        if a[i] == x {
            print!(" {}", i + 1);
        }
    }
    if count == 0 {
        print!(" none");
    }
    println!();
}
