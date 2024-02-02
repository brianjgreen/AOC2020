// Advent of Code 2023 - Day 1
// Rust solution: 1 Dec 2023 Brian Green
//
// Problem 1: What is the sum of all of the calibration values?
// Problem 2: What is the sum of all of the calibration values? (include numbers spelled out as words)
use std::collections::HashMap;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

// Read text file and return each line as an element in an array (vector)
fn lines_from_file() -> Vec<String> {
    let file = File::open("data.dat").expect("Unable to read data file.");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

// Convert spelled out numbers from words to digits
// Note that some of the words overlap, substitution may corrupt the second word
fn word_to_digit(value: &str) -> String {
    let num_name: HashMap<&str, &str> = HashMap::from([
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);

    let no_word = " ";
    let mut min_word = (128, no_word);
    let mut max_word = (0, no_word);
    for key in num_name.keys() {
        // Get a list of locations in the string where the word appears
        let word_locations: Vec<_> = value.match_indices(key).collect();
        for (loc_key, loc_value) in word_locations {
            // Find the first instance of a digit word
            if loc_key < min_word.0 {
                min_word = (loc_key, loc_value);
            }
            // Find the last instance of a digit word
            if loc_key > max_word.0 {
                max_word = (loc_key, loc_value);
            }
        }
    }
    let mut new_value = value.to_owned();
    // Replace the first and last digit words with the digit (e.g one -> 1)
    if min_word.1 != no_word {
        // Double the last char in a digit word, inject that into the string so that the overlapping digit word is preserved
        // e.g. oneight -> oneeight
        let append_char = min_word.1.chars().last().unwrap().to_string();
        let new_char = min_word.1;
        new_value = str::replacen(
            &new_value,
            min_word.1,
            &(new_char.to_owned() + &append_char),
            1,
        );
        new_value = str::replacen(&new_value, min_word.1, num_name[min_word.1], 1);
    }
    if max_word.1 != no_word {
        new_value = str::replace(&new_value, max_word.1, num_name[max_word.1]);
    }
    new_value
}

// Find the first and last digits in each line
// Note that if there is only one digit in a line, it is both first and last
fn get_calibration_value(value: &str) -> i32 {
    let mut found_first: bool = false;
    let mut first = ' ';
    let mut last = ' ';
    for digit in value.chars() {
        if digit.is_ascii_digit() {
            if !found_first {
                first = digit;
                last = digit;
                found_first = true;
            } else {
                last = digit;
            }
        }
    }
    let calibration = first.to_string() + &last.to_string();
    calibration.parse::<i32>().unwrap()
}

// Sum the first and last digits in each line
fn get_calibration(calculations: &Vec<String>) -> i32 {
    let mut total_calc: i32 = 0;
    for value in calculations {
        total_calc += get_calibration_value(value);
    }
    total_calc
}

// Sum the first and last digits in each line, include digits spelled out as words (e.g. "eight")
fn get_calibration_words(calculations: &Vec<String>) -> i32 {
    let mut total_calc: i32 = 0;
    for value in calculations {
        total_calc += get_calibration_value(&word_to_digit(value));
    }
    total_calc
}

fn main() -> std::io::Result<()> {
    let calculations = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_calibration(&calculations));
    // Part 2
    println!("Part 2 = {}", get_calibration_words(&calculations));
    Ok(())
}
