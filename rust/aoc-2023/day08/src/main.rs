// Advent of Code 2023 - Day 7
// Rust solution: 7 Dec 2023 Brian Green
//
// Problem 1: What are the total winnings??
// Problem 2: ?
use std::collections::HashMap;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

// Return a Vector of Strings, each element is a String of a row of data
fn lines_from_file() -> Vec<String> {
    let file = File::open("data.dat").expect("Unable to read data file.");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn get_num_steps(path_map: &Vec<String>, part2: bool) -> u64 {
    let directions = &path_map[0];
    let mut left_dir: HashMap<String, String> = HashMap::new();
    let mut right_dir: HashMap<String, String> = HashMap::new();
    for map_dir in 2..path_map.len() {
        let map_dir_format: Vec<&str> = path_map[map_dir].split(" = ").collect();
        let key: String = map_dir_format[0].to_string();
        let left_right_raw = map_dir_format[1].replace("(", "").replace(")", "");
        let left_right_format: Vec<&str> = left_right_raw.split(", ").collect();
        left_dir.insert(key.clone(), left_right_format[0].to_string());
        right_dir.insert(key.clone(), left_right_format[1].to_string());
    }
    let mut current: String = "AAA".to_string();
    let mut all_curr: Vec<String> = Vec::new();
    let mut all_done: Vec<String> = Vec::new();
    let mut count: u64 = 0; 
    let next_char: Vec<char> = directions.chars().collect();

    for i in left_dir.keys() {
        let dest: Vec<char> = i.chars().collect();
        if dest[2] == 'A' {
            all_curr.push(i.to_string());
        } else if dest[2] == 'Z' {
            all_done.push(i.to_string());
        }
    }
    println!("{:?}", all_curr);
    println!("{:?}", all_done);
    loop {
        if count % 100000 == 0 {
            println!("{}", count);
        }
        for i in 0..directions.len() {
            count += 1;
            if part2 {
                let mut z_done: bool = true;
                for j in 0..all_curr.len() {
                    if next_char[i] == 'L' {
                        all_curr[j] = left_dir.get(&all_curr[j]).unwrap().to_string();
                    } else {
                        all_curr[j] = right_dir.get(&all_curr[j]).unwrap().to_string();
                    }
                    if !all_done.contains(&all_curr[j]) {
                        z_done = false;
                    }
                }
                // println!("{:?}", all_curr);
                if z_done {
                    return count;
                }
            } else {
                if next_char[i] == 'L' {
                    current = left_dir.get(&current).unwrap().to_string();
                } else {
                    current = right_dir.get(&current).unwrap().to_string();
                }
                if current == "ZZZ" {
                    return count;
                } 
            }
        }
    }
}

fn main() -> std::io::Result<()> {
    let path_map = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_num_steps(&path_map, false));
    // Part 2
    println!("Part 2 = {}", get_num_steps(&path_map, true));
    Ok(())
}
