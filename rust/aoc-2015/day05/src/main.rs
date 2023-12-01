// Advent of Code 2015 - Day 5
// Python solution: 17 Nov 2021 Brian Green
// Rust solution: 1 Dec 2023 Brian Green
//
// Problem 1: How many strings are nice?
// Problem 2: How many strings are nice? (alternate rules)
// pub(crate) use std::fs;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

fn lines_from_file() -> Vec<String> {
    let file = File::open("data.dat").expect("Unable to read data file.");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

// Return the number of vowels in a message
fn num_vowels(message: &String) -> usize {
    let mut num_vowels = 0;
    for letter in "aeiou".chars() {
        num_vowels += message.matches(letter).count();
    }
    return num_vowels;
}

// Return the number of double chars in a message
fn num_doubles(message: &String) -> usize {
    let mut num_doubles = 0;
    let letters: Vec<char> = message.chars().collect();
    for i in 0..letters.len() - 1 {
        if letters[i] == letters[i + 1] {
            num_doubles += 1;
        }
    }
    return num_doubles;
}

// Return true if any of the naughty strings are in a message
fn contains_naugty_string(message: &String) -> bool {
    let naughty = ["ab", "cd", "pq", "xy"];
    for bad in naughty {
        if message.contains(bad) {
            return true;
        }
    }
    return false;
}

// Find the number of nice messages based on Part 1 rules
fn num_nice(letters: &Vec<String>) -> u32 {
    let mut total_nice = 0;
    for entry in letters {
        // Contains at least three vowels (aeiou only)
        if num_vowels(&entry) < 3 {
            continue;
        }
        // Contains at least one letter that appears twice in a row
        if num_doubles(&entry) == 0 {
            continue;
        }
        // Does not contain the strings ab, cd, pq, or xy
        if contains_naugty_string(&entry) {
            continue;
        }
        total_nice += 1;
    }
    return total_nice;
}

// Return the number of identical non-overlapping pairs of chars
fn num_pairs(message: &String) -> usize {
    let mut num_pairs = 0;
    for i in 0..message.len() - 2 {
        if message[i + 2..].contains(&message[i..i + 2]) {
            num_pairs += 1;
        }
    }
    return num_pairs;
}

// Return the number of doubles with one char between them
fn num_gap_doubles(message: &String) -> usize {
    let mut num_doubles = 0;
    let letters: Vec<char> = message.chars().collect();
    for i in 0..letters.len() - 2 {
        if letters[i] == letters[i + 2] {
            num_doubles += 1;
        }
    }
    return num_doubles;
}

// Find the number of nice messages based on Part 2 rules
fn num_nice_alternate(letters: &Vec<String>) -> u32 {
    let mut total_nice = 0;
    for entry in letters {
        // Contains a pair of any two letters that appears at least twice in the string without overlapping
        if num_pairs(&entry) == 0 {
            continue;
        }
        // Contains at least one letter which repeats with exactly one letter between them
        if num_gap_doubles(&entry) == 0 {
            continue;
        }
        total_nice += 1;
    }
    return total_nice;
}

fn main() -> std::io::Result<()> {
    let letters = lines_from_file();
    // Part 1
    println!("Part 1 = {}", num_nice(&letters));
    // Part 2
    println!("Part 2 = {}", num_nice_alternate(&letters));
    Ok(())
}
