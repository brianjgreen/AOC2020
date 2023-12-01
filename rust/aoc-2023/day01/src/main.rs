// Advent of Code 2023 - Day 1
// Rust solution: 1 Dec 2023 Brian Green
//
// Problem 1: What is the sum of all of the calibration values?
// Problem 2: How many total feet of ribbon should they order?
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


fn get_calibration(calculations: &Vec<String>) -> i32 {
    let mut total_calc: i32 = 0;
    for value in calculations {
        let mut found_first: bool = false;
        let mut first = ' ';
        let mut last = ' ';
        for digit in value.chars() {
            if digit.is_digit(10) {
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
        total_calc += calibration.parse::<i32>().unwrap();
    }
    return total_calc;
}


fn main() -> std::io::Result<()> {
    let calculations = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_calibration(&calculations));
    // Part 2
    // println!("Part 2 = {}", get_ribbon(&dimensions));
    Ok(())
}
