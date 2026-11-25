use std::io::Read;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut queue: Vec<&str> = Vec::new();
    let mut head = 0;
    for _ in 0..n {
        let cmd = tokens.next().unwrap();
        if cmd == "join" {
            queue.push(tokens.next().unwrap());
        } else if head < queue.len() {
            println!("served {}", queue[head]);
            head += 1;
        } else {
            println!("nobody waiting");
        }
    }
    if head == queue.len() {
        println!("waiting: none");
    } else {
        println!("waiting: {}", queue[head..].join(" "));
    }
}
