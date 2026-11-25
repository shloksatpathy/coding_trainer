use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let r: usize = words.next().unwrap().parse().unwrap();
    let c: usize = words.next().unwrap().parse().unwrap();
    let mut g = vec![vec![0i64; c]; r];
    for i in 0..r {
        for j in 0..c {
            g[i][j] = words.next().unwrap().parse().unwrap();
        }
    }
    let mut best = vec![vec![0i64; c]; r];
    for i in 0..r {
        for j in 0..c {
            if i == 0 && j == 0 {
                best[i][j] = g[i][j];
            } else if i == 0 {
                best[i][j] = best[i][j - 1] + g[i][j];
            } else if j == 0 {
                best[i][j] = best[i - 1][j] + g[i][j];
            } else {
                best[i][j] = best[i - 1][j].min(best[i][j - 1]) + g[i][j];
            }
        }
    }
    println!("{}", best[r - 1][c - 1]);
}
