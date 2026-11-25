use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let line = input.lines().next().unwrap();
    let mut count = [0; 26];
    for b in line.bytes() {
        if b.is_ascii_alphabetic() {
            count[(b.to_ascii_lowercase() - b'a') as usize] += 1;
        }
    }
    let mut order: Vec<usize> = Vec::new();
    for i in 0..26 {
        if count[i] > 0 {
            order.push(i);
        }
    }
    order.sort_by(|&x, &y| count[y].cmp(&count[x]).then(x.cmp(&y)));
    for i in order {
        println!("{}: {}", (b'a' + i as u8) as char, count[i]);
    }
}
