use std::io::Read;

struct Fraction {
    num: i64,
    den: i64,
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn add(f: &Fraction, g: &Fraction) -> Fraction {
    let num = f.num * g.den + g.num * f.den;
    let den = f.den * g.den;
    let k = gcd(num, den);
    Fraction { num: num / k, den: den / k }
}

fn parse(text: &str) -> Fraction {
    let mut parts = text.split('/');
    let num = parts.next().unwrap().parse().unwrap();
    let den = parts.next().unwrap().parse().unwrap();
    Fraction { num, den }
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let f = parse(words.next().unwrap());
    let g = parse(words.next().unwrap());
    let s = add(&f, &g);
    println!("{}/{}", s.num, s.den);
}
