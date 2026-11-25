use std::io::Read;

fn wins(g: &Vec<&[u8]>, p: u8) -> bool {
    for i in 0..3 {
        if g[i][0] == p && g[i][1] == p && g[i][2] == p {
            return true;
        }
        if g[0][i] == p && g[1][i] == p && g[2][i] == p {
            return true;
        }
    }
    if g[0][0] == p && g[1][1] == p && g[2][2] == p {
        return true;
    }
    g[0][2] == p && g[1][1] == p && g[2][0] == p
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut g: Vec<&[u8]> = Vec::new();
    for _ in 0..3 {
        g.push(words.next().unwrap().as_bytes());
    }
    let mut full = true;
    for i in 0..3 {
        for j in 0..3 {
            if g[i][j] == b'.' {
                full = false;
            }
        }
    }
    if wins(&g, b'X') {
        println!("X wins");
    } else if wins(&g, b'O') {
        println!("O wins");
    } else if full {
        println!("draw");
    } else {
        println!("in progress");
    }
}
