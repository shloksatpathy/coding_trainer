use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let r: usize = words.next().unwrap().parse().unwrap();
    let c: usize = words.next().unwrap().parse().unwrap();
    let mut g: Vec<Vec<i64>> = Vec::new();
    for _ in 0..r {
        let mut row = Vec::new();
        for _ in 0..c {
            row.push(words.next().unwrap().parse::<i64>().unwrap());
        }
        g.push(row);
    }
    let mut best = g[0][0];
    let mut br = 0;
    let mut bc = 0;
    for i in 0..r {
        for j in 0..c {
            if g[i][j] > best {
                best = g[i][j];
                br = i;
                bc = j;
            }
        }
    }
    println!("max: {} at {} {}", best, br + 1, bc + 1);
}
