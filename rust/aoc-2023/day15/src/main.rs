// Advent of Code 2023 - Day 15
// Rust solution: 15 Dec 2023 Brian Green
//
// Problem 1: What is the sum of the results?
// Problem 2:
//use std::collections::HashMap;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

// Return a Vector of Strings, each element is a String of a row of data
fn lines_from_file(filename: String) -> Vec<String> {
    let file = File::open(filename).expect("Unable to read data file.");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

// Calculate the hash of the string
fn get_hash(curr_hash: &str) -> i64 {
    let mut curr_val = 0;
    for c in curr_hash.bytes() {
        // Determine the ASCII code for the current character of the string.
        // Increase the current value by the ASCII code you just determined.
        curr_val += c as i64;

        // Set the current value to itself multiplied by 17.
        curr_val *= 17;

        // Set the current value to the remainder of dividing itself by 256.
        curr_val %= 256;

        if curr_val > 255 {
            println!("ERROR!!! Value is over 255:{}", curr_val);
        }
    }
    curr_val
}

// Split the string by commas, sum the calculations of each hash
fn sum_of_hashes(hash_data: &[String]) -> i64 {
    let mut sum_results: i64 = 0;
    let all_hashes: Vec<&str> = hash_data[0].split(',').collect();
    for curr_hash in all_hashes {
        sum_results += get_hash(curr_hash);
    }
    sum_results
}

fn main() -> std::io::Result<()> {
    let hash_data = lines_from_file("data.dat".to_string());
    // Part 1
    println!("Part 1 = {}", sum_of_hashes(&hash_data));
    // Part 2
    // println!("Part 2 = {}", sum_of_values(&history, true));
    Ok(())
}
