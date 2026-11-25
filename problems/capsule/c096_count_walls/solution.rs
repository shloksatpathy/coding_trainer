use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let r: usize = words.next().unwrap().parse().unwrap();
    let c: usize = words.next().unwrap().parse().unwrap();
    let mut g: Vec<&[u8]> = Vec::new();
    for _ in 0..r {
        g.push(words.next().unwrap().as_bytes());
    }
    let mut total = 0;
    for i in 0..r {
        let mut count = 0;
        for j in 0..c {
            if g[i][j] == b'#' {
                count += 1;
            }
        }
        println!("{}", count);
        total += count;
    }
    println!("total: {}", total);
}
