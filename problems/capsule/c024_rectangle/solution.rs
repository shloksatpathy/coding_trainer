use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let w: f64 = words.next().unwrap().parse().unwrap();
    let h: f64 = words.next().unwrap().parse().unwrap();
    println!("area: {:.2}", w * h);
    println!("perimeter: {:.2}", 2.0 * (w + h));
}
