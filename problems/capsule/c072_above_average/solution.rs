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
    let mut total: i64 = 0;
    for i in 0..n {
        total += a[i];
    }
    println!("average: {:.2}", total as f64 / n as f64);
    let mut found = 0;
    for i in 0..n {
        if a[i] * n as i64 > total {
            if found > 0 {
                print!(" ");
            }
            print!("{}", a[i]);
            found += 1;
        }
    }
    if found == 0 {
        println!("none");
    } else {
        println!();
    }
}
