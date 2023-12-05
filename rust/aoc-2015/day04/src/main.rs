// Advent of Code 2015 - Day 4
// Python solution: 17 Nov 2021 Brian Green
// Rust solution: 30 Nov 2023 Brian Green
//
// Problem 1: lowest positive number that produces such a hash starting with 5 zeros
// Problem 2: same but starting with 6 zeros

use md5;

fn find_hash(size: usize) -> i32 {
    let mut base = -1;
    loop {
        base += 1;
        let base_hex = format!("{}", base);
        let secret = "iwrupvqb".to_owned() + &base_hex;
        let hash = format!("{:x}", md5::compute(&secret));
        let compare = "0".repeat(size);
        if hash[0..size] == compare.to_owned() {
            return base;
        }
    }
}

fn main() {
    // Part 1
    println!("Part 1 = {}", find_hash(5));
    // Part 2
    println!("Part 2 = {}", find_hash(6));
}
