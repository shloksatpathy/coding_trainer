use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut count = 0;
    for w in input.split_whitespace() {
        if count > 0 {
            print!("-");
        }
        print!("{}", w);
        count += 1;
    }
    println!();
}
