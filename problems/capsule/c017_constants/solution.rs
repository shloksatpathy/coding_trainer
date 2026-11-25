use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    const SECONDS_PER_MINUTE: i64 = 60;
    const MS_PER_SECOND: i64 = 1000;
    let m: i64 = input.trim().parse().unwrap();
    let s = m * SECONDS_PER_MINUTE;
    println!("{} seconds", s);
    println!("{} milliseconds", s * MS_PER_SECOND);
}
