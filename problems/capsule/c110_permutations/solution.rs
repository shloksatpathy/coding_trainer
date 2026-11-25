use std::io::Read;

fn perm(cur: &mut Vec<usize>, used: &mut Vec<bool>, n: usize) {
    if cur.len() == n {
        for i in 0..n {
            if i > 0 {
                print!(" ");
            }
            print!("{}", cur[i]);
        }
        println!();
        return;
    }
    for x in 1..=n {
        if !used[x] {
            used[x] = true;
            cur.push(x);
            perm(cur, used, n);
            cur.pop();
            used[x] = false;
        }
    }
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut cur: Vec<usize> = Vec::new();
    let mut used = vec![false; n + 1];
    perm(&mut cur, &mut used, n);
}
