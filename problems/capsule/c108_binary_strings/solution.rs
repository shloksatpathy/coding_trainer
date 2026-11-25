use std::io::Read;

fn gen(buf: &mut Vec<u8>, pos: usize) {
    if pos == buf.len() {
        println!("{}", String::from_utf8(buf.clone()).unwrap());
        return;
    }
    buf[pos] = b'0';
    gen(buf, pos + 1);
    buf[pos] = b'1';
    gen(buf, pos + 1);
}

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    let mut buf = vec![b'0'; n];
    gen(&mut buf, 0);
}
