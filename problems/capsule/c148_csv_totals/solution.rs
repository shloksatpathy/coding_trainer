use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut depts: Vec<&str> = Vec::new();
    let mut totals: Vec<i64> = Vec::new();
    let mut overall = 0;
    for _ in 0..n {
        let mut fields = lines.next().unwrap().split(',');
        fields.next();
        let dept = fields.next().unwrap();
        let amount: i64 = fields.next().unwrap().trim().parse().unwrap();
        let mut k = 0;
        while k < depts.len() && depts[k] != dept {
            k += 1;
        }
        if k == depts.len() {
            depts.push(dept);
            totals.push(0);
        }
        totals[k] += amount;
        overall += amount;
    }
    for k in 0..depts.len() {
        println!("{}: {}", depts[k], totals[k]);
    }
    println!("overall: {}", overall);
}
