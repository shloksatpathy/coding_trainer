use std::io::Read;

fn back(w: &[u8], i: usize) {
    if i == w.len() {
        return;
    }
    back(w, i + 1);
    print!("{}", w[i] as char);
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let w = input.trim().as_bytes();
    back(w, 0);
    println!();
}
