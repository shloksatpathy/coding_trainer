use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut ways: Vec<i64> = vec![0; n + 1];
    ways[0] = 1;
    ways[1] = 1;
    for i in 2..=n {
        ways[i] = ways[i - 1] + ways[i - 2];
    }
    println!("{}", ways[n]);
}
