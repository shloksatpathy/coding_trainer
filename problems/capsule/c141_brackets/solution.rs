use std::io::Read;

fn opener(close: char) -> char {
    if close == ')' {
        return '(';
    }
    if close == ']' {
        return '[';
    }
    '{'
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let line = input.lines().next().unwrap_or("");
    let mut stack: Vec<char> = Vec::new();
    let mut ok = true;
    for ch in line.chars() {
        if ch == '(' || ch == '[' || ch == '{' {
            stack.push(ch);
        } else if ch == ')' || ch == ']' || ch == '}' {
            if stack.pop() != Some(opener(ch)) {
                ok = false;
                break;
            }
        }
    }
    if ok && stack.is_empty() {
        println!("yes");
    } else {
        println!("no");
    }
}
