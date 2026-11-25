use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut a: Vec<i64> = Vec::new();
    for _ in 0..n {
        a.push(words.next().unwrap().parse().unwrap());
    }
    let q: usize = words.next().unwrap().parse().unwrap();
    for _ in 0..q {
        let x: i64 = words.next().unwrap().parse().unwrap();
        let mut lo: i64 = 0;
        let mut hi: i64 = n as i64 - 1;
        let mut pos: i64 = -1;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if a[mid as usize] == x {
                pos = mid + 1;
                break;
            }
            if a[mid as usize] < x {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        println!("{}", pos);
    }
}
