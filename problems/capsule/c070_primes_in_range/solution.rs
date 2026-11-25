use std::io::Read;

fn is_prime(n: i64) -> bool {
    if n < 2 {
        return false;
    }
    let mut i = 2;
    while i * i <= n {
        if n % i == 0 {
            return false;
        }
        i += 1;
    }
    true
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a: i64 = words.next().unwrap().parse().unwrap();
    let b: i64 = words.next().unwrap().parse().unwrap();
    let mut found = 0;
    for x in a..=b {
        if is_prime(x) {
            if found > 0 {
                print!(" ");
            }
            print!("{}", x);
            found += 1;
        }
    }
    if found == 0 {
        println!("none");
    } else {
        println!();
    }
}
