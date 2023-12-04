// Advent of Code 2023 - Day 3
// Rust solution: 3 Dec 2023 Brian Green
//
// Problem 1: What is the sum of all of the part numbers in the engine schematic?
// Problem 2: What is the sum of all of the gear ratios in your engine schematic?
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

// Return the sum of the part numbers and the sum of the products of gear ratios
fn sum_of_part_nums(lines: &Vec<String>) -> (u32, u32) {
    let max_x = lines[0].len() + 1;
    let max_y = lines.len();
    let mut sum_part_nums: u32 = 0; // Part 1
    let mut sum_prod_gears: u32 = 0; // Part 2
    let mut prod_gears = HashMap::new(); // Need to optmize this code, should be able to use one HashMap with Vectors
    let mut num_gears = HashMap::new();
    for y in 0..max_y {
        let mut part_no: u32 = 0;
        let mut new_part: bool = true;
        let mut part_in_progress: bool = false;
        let mut start_x: usize = 0;
        let mut start_y: usize = 0;
        let mut row: Vec<char> = lines[y].chars().collect();
        row.push('.'); // Fix for part numbers at the end of a line
        for x in 0..max_x {
            let point: char = row[x];
            if point.is_digit(10) {
                if new_part {
                    new_part = false;
                    part_in_progress = true;
                    if x == 0 {
                        // Stay in bounds of array
                        start_x = 0;
                    } else {
                        start_x = x - 1;
                    }
                    if y == 0 {
                        // Stay in bounds of array
                        start_y = 0;
                    } else {
                        start_y = y - 1;
                    }
                    part_no = point.to_digit(10).unwrap();
                } else {
                    part_no = part_no * 10 + point.to_digit(10).unwrap();
                }
            } else {
                // Need a fix to deal with parsing part numbers at the end of the line
                // Using workaround of adding a "." to the end of every line
                if part_in_progress {
                    part_in_progress = false;
                    new_part = true;
                    let mut end_x = x + 1;
                    if end_x > max_x {
                        // Stay in bounds of array
                        end_x = max_x;
                    }
                    let mut end_y = y + 2;
                    if end_y > max_y {
                        // Stay in bounds of array
                        end_y = max_y;
                    }
                    let mut valid_part_no: bool = false;
                    for k in start_y..end_y {
                        let mut y_zone: Vec<char> = lines[k].chars().collect();
                        y_zone.push('.'); // Fix for part numbers at the end of the line
                        for j in start_x..end_x {
                            let check_point: char = y_zone[j];
                            if !check_point.is_digit(10) && check_point != '.' {
                                // A valid part number is next to a char that is not a digit or a "."
                                valid_part_no = true;
                                if check_point == '*' {
                                    // For part 2, count up how many part numbers are next to a "*"
                                    let count = num_gears.entry((j, k)).or_insert(0);
                                    *count += 1;
                                    // Multiply the part numbers together if they are next to a "*"
                                    let product = prod_gears.entry((j, k)).or_insert(1);
                                    *product *= part_no;
                                }
                            }
                        }
                    }
                    if valid_part_no {
                        // Part 1
                        sum_part_nums += part_no;
                    }
                }
            }
        }
    }
    for (key, value) in num_gears {
        // Part 2
        if value == 2 {
            sum_prod_gears += prod_gears[&key];
        }
    }
    return (sum_part_nums, sum_prod_gears);
}

fn main() -> std::io::Result<()> {
    let map_of_parts = lines_from_file();
    // Parts 1 and 2
    let (parts, gears) = sum_of_part_nums(&map_of_parts);
    println!("Part 1 = {}, Part 2 = {}", parts, gears);

    Ok(())
}
