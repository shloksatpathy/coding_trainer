use std::io::Read;

struct Time {
    h: i64,
    m: i64,
}

fn to_minutes(t: &Time) -> i64 {
    t.h * 60 + t.m
}

fn parse(text: &str) -> Time {
    let mut parts = text.split(':');
    let h = parts.next().unwrap().parse().unwrap();
    let m = parts.next().unwrap().parse().unwrap();
    Time { h, m }
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let a = parse(words.next().unwrap());
    let b = parse(words.next().unwrap());
    let d = to_minutes(&b) - to_minutes(&a);
    println!("{}:{:02}", d / 60, d % 60);
}
