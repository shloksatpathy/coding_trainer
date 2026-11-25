use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let line = input.lines().next().unwrap().as_bytes();
    let mut last = [-1i64; 256];
    let mut start: i64 = 0;
    let mut best = 0;
    for i in 0..line.len() {
        let ch = line[i] as usize;
        if last[ch] >= start {
            start = last[ch] + 1;
        }
        last[ch] = i as i64;
        if i as i64 - start + 1 > best {
            best = i as i64 - start + 1;
        }
    }
    println!("{}", best);
}
