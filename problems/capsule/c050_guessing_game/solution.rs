use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let secret: i64 = words.next().unwrap().parse().unwrap();
    let n: i64 = words.next().unwrap().parse().unwrap();
    let mut found = false;
    for k in 1..=n {
        let g: i64 = words.next().unwrap().parse().unwrap();
        if g < secret {
            println!("too low");
        } else if g > secret {
            println!("too high");
        } else {
            println!("correct on guess {}", k);
            found = true;
            break;
        }
    }
    if !found {
        println!("no luck, it was {}", secret);
    }
}
