// Advent of Code 2023 - Day 9
// Rust solution: 10 Dec 2023 Brian Green
//
// Problem 1: What is the sum of these extrapolated values??
// Problem 2: ?
//use std::collections::HashMap;
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

fn get_next_value(sequence: &Vec<i64>) -> i64 {
    println!("{:?}", sequence);
    let mut new_seq: Vec<i64> = Vec::new();
    let mut all_zeros: bool = true;
    for i in sequence {
        if i != 0 {
            all_zeros = false;
            break;
        }
    }
    if all_zeros {
        return 0;
    }
    
    0
}

fn sum_of_values(history: &Vec<String>) -> i64 {
    let mut sum_vals: i64 = 0;
    for sequence in history {
        let seq: Vec<i64> = sequence
            .split(" ")
            .map(|x| x.parse::<i64>().unwrap())
            .collect();
        sum_vals += get_next_value(&seq);
    }
    sum_vals
}

fn main() -> std::io::Result<()> {
    let history = lines_from_file();
    // Part 1
    println!("Part 1 = {}", sum_of_values(&history));
    // Part 2
    // println!("Part 2 = {}", get_num_steps(&path_map, true));
    Ok(())
}
