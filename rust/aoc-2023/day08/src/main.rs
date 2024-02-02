// Advent of Code 2023 - Day 8
// Rust solution: 8 Dec 2023 Brian Green
//
// Problem 1: How many steps are required to reach ZZZ?
// Problem 2: How many steps does it take before you're only on nodes that end with Z?
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

// https://github.com/TheAlgorithms/Rust/blob/master/src/math/lcm_of_n_numbers.rs
// Modified to use u64 instead of usize
// Could not figure out how to use the crate num::integer::lcm but this is similar
fn lcm(nums: &[u64]) -> u64 {
    if nums.len() == 1 {
        return nums[0];
    }
    let a = nums[0];
    let b = lcm(&nums[1..]);
    a * b / gcd_of_two_numbers(a, b)
}

// https://github.com/TheAlgorithms/Rust/blob/master/src/math/lcm_of_n_numbers.rs
// Modified to use u64 instead of usize
// Could not figure out how to use the crate num::integer::lcm but this is similar
fn gcd_of_two_numbers(a: u64, b: u64) -> u64 {
    if b == 0 {
        return a;
    }
    gcd_of_two_numbers(b, a % b)
}

// Parse the directions and the path map from the data file
// Part 1 sum the steps to get from AAA to ZZZ
// Part 2 A ghost starts at every location ending in A. Calc the number of steps needed for all ghosts
// to appear at a location ending in Z all at the same time.
// Would have liked to break this down into smaller function calls but struggling with the ownership of strings
// Brute force takes way too long. Figured out the pattern of the ghost travel path cycles were a multiple of
// the length of the directions. After some debug and experimentation, figured out the quick way is to find the
// least common multiplier of the number of steps each ghost takes to get from xxA to xxZ
fn get_num_steps(path_map: &[String], part2: bool) -> u64 {
    let directions = &path_map[0];
    let mut left_dir: HashMap<String, String> = HashMap::new();
    let mut right_dir: HashMap<String, String> = HashMap::new();
    for path_map_dir in path_map.iter().skip(2) {
        let map_dir_format: Vec<&str> = path_map_dir.split(" = ").collect();
        let key: String = map_dir_format[0].to_string();
        let left_right_raw = map_dir_format[1].replace(['(', ')'], "");
        let left_right_format: Vec<&str> = left_right_raw.split(", ").collect();
        left_dir.insert(key.clone(), left_right_format[0].to_string());
        right_dir.insert(key.clone(), left_right_format[1].to_string());
    }
    let mut current: String = "AAA".to_string(); // Part 1
    let mut all_curr: Vec<String> = Vec::new(); // Part 2 - Start one ghost at every xxA
    let mut all_done: Vec<String> = Vec::new(); // Part 2 - End all ghosts at any xxZ
    let mut count: u64 = 0;
    let next_char: Vec<char> = directions.chars().collect();
    let mut ghost_path: Vec<u64> = Vec::new(); // Part 2 - Each ghost path # of steps per cycle
    for i in left_dir.keys() {
        let dest: Vec<char> = i.chars().collect();
        if dest[2] == 'A' {
            all_curr.push(i.to_string()); // Part 2 - Start at every xxA
        } else if dest[2] == 'Z' {
            all_done.push(i.to_string()); // Part 2 - End at every xxZ
        }
    }
    loop {
        for this_char in next_char.iter().take(directions.len()) {
            count += 1;
            if part2 {
                for this_ghost in &mut all_curr {
                    if *this_char == 'L' {
                        // There must be a way to optmize this ownership of strings
                        *this_ghost = left_dir.get(this_ghost).unwrap().to_string();
                    } else {
                        *this_ghost = right_dir.get(this_ghost).unwrap().to_string();
                    }
                    if all_done.contains(this_ghost) {
                        // Ghost completed one whole path cycle
                        ghost_path.push(count);
                    }
                }
                if ghost_path.len() == all_done.len() {
                    // Find the lowest common multiple of all of the ghost cycles
                    return lcm(&ghost_path);
                }
            } else {
                // Part 1
                if *this_char == 'L' {
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
