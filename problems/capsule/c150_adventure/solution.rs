use std::io::Read;

const ROOMS: [&str; 5] = ["hall", "kitchen", "library", "garden", "vault"];
const DIRS: [&str; 4] = ["north", "east", "south", "west"];
const EXITS: [[i64; 4]; 5] = [[2, -1, 3, 1], [-1, 0, -1, -1], [-1, 4, 0, -1], [0, -1, -1, -1], [-1, -1, -1, -1]];
const VAULT: usize = 4;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut room = 0;
    let mut key_room: i64 = 3;
    let mut has_key = false;
    for _ in 0..n {
        let mut words = lines.next().unwrap().split_whitespace();
        let cmd = words.next().unwrap();
        if cmd == "go" {
            let arg = words.next().unwrap();
            let mut d = 0;
            while d < 4 && DIRS[d] != arg {
                d += 1;
            }
            if d == 4 || EXITS[room][d] == -1 {
                println!("You can't go {}.", arg);
            } else if EXITS[room][d] == VAULT as i64 && !has_key {
                println!("The vault is locked.");
            } else {
                room = EXITS[room][d] as usize;
                println!("You are in the {}.", ROOMS[room]);
                if room == VAULT {
                    println!("You found the treasure!");
                    break;
                }
            }
        } else if cmd == "take" {
            if key_room == room as i64 {
                println!("You take the key.");
                has_key = true;
                key_room = -1;
            } else {
                println!("There is no key here.");
            }
        } else {
            print!("{}: exits", ROOMS[room]);
            for d in 0..4 {
                if EXITS[room][d] != -1 {
                    print!(" {}", DIRS[d]);
                }
            }
            if key_room == room as i64 {
                print!(" (key here)");
            }
            println!();
        }
    }
    if room != VAULT {
        println!("You give up in the {}.", ROOMS[room]);
    }
}
