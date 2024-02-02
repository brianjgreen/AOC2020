// Advent of Code 2023 - Day 9
// Rust solution: 11 Dec 2023 Brian Green
//
// Problem 1: What is the sum of these extrapolated values? (end)
// Problem 2: What is the sum of these extrapolated values? (beginning)
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

// Recursive function to determine the next value of the sequence (part 1) or first value (part 2)
fn get_next_value(sequence: &Vec<i64>, part2: bool) -> i64 {
    let mut new_seq: Vec<i64> = Vec::new();

    // Check to see if the sequence is all zeros
    let mut all_zeros: bool = true;
    for i in sequence {
        if i != &0 {
            all_zeros = false;
            break;
        }
    }
    if all_zeros {
        return 0;
    }

    // Calcualte the next sequence using the difference between each adjacent value
    let mut left_e = sequence[0];
    for right_e in sequence.iter().skip(1) {
        new_seq.push(right_e - left_e);
        left_e = *right_e;
    }
    if part2 {
        // Find the first value in the sequence
        sequence[0] - get_next_value(&new_seq, part2)
    } else {
        // Find the last value in the sequence
        left_e + get_next_value(&new_seq, part2)
    }
}

// Convert strings into integers, sum the last (part 1) or first (part 2) value of the sequence
fn sum_of_values(history: &Vec<String>, part2: bool) -> i64 {
    let mut sum_vals: i64 = 0;
    for sequence in history {
        let seq: Vec<i64> = sequence
            .split(' ')
            .map(|x| x.parse::<i64>().unwrap())
            .collect();
        sum_vals += get_next_value(&seq, part2);
    }
    sum_vals
}

fn main() -> std::io::Result<()> {
    let history = lines_from_file();
    // Part 1
    println!("Part 1 = {}", sum_of_values(&history, false));
    // Part 2
    println!("Part 2 = {}", sum_of_values(&history, true));
    Ok(())
}
