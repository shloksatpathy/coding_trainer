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
    let mut swaps = 0;
    let mut swapped = true;
    while swapped {
        swapped = false;
        for i in 0..n - 1 {
            if a[i] > a[i + 1] {
                a.swap(i, i + 1);
                swaps += 1;
                swapped = true;
            }
        }
    }
    for i in 0..n {
        if i > 0 {
            print!(" ");
        }
        print!("{}", a[i]);
    }
    println!();
    println!("swaps: {}", swaps);
}
