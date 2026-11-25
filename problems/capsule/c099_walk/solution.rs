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
    let moves = words.next().unwrap();
    let mut row: i64 = 0;
    let mut col: i64 = 0;
    let mut moved = 0;
    for m in moves.chars() {
        let mut nr = row;
        let mut nc = col;
        if m == 'U' {
            nr -= 1;
        } else if m == 'D' {
            nr += 1;
        } else if m == 'L' {
            nc -= 1;
        } else {
            nc += 1;
        }
        if nr >= 0 && nr < r as i64 && nc >= 0 && nc < c as i64 && g[nr as usize][nc as usize] == b'.' {
            row = nr;
            col = nc;
            moved += 1;
        }
    }
    println!("at {} {}", row + 1, col + 1);
    println!("moved: {}", moved);
}
