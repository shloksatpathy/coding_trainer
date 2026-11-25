use std::io::Read;

fn area(w: i64, h: i64) -> i64 {
    w * h
}

fn draw_box(w: i64, h: i64) {
    for _ in 0..h {
        for _ in 0..w {
            print!("*");
        }
        println!();
    }
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let w: i64 = words.next().unwrap().parse().unwrap();
    let h: i64 = words.next().unwrap().parse().unwrap();
    println!("area: {}", area(w, h));
    draw_box(w, h);
}
