use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let w = input.trim();
    let b = w.as_bytes();
    let mut i = 0;
    let mut j = b.len() - 1;
    let mut same = true;
    while i < j {
        if b[i] != b[j] {
            same = false;
            break;
        }
        i += 1;
        j -= 1;
    }
    if same {
        println!("yes");
    } else {
        println!("no");
    }
}
