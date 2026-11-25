use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut g: Vec<Vec<i64>> = Vec::new();
    for _ in 0..n {
        let mut row = Vec::new();
        for _ in 0..n {
            row.push(words.next().unwrap().parse::<i64>().unwrap());
        }
        g.push(row);
    }
    let mut main_sum = 0;
    let mut anti = 0;
    for i in 0..n {
        main_sum += g[i][i];
        anti += g[i][n - 1 - i];
    }
    println!("main: {}", main_sum);
    println!("anti: {}", anti);
}
