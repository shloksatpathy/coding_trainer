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
    for i in 0..r {
        let mut total = 0;
        for j in 0..c {
            if j > 0 {
                print!(" ");
            }
            print!("{}", g[i][j]);
            total += g[i][j];
        }
        println!(" | {}", total);
    }
}
