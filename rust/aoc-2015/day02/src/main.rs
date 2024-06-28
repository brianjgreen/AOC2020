// Advent of Code 2015 - Day 2
// Python solution: 16 Nov 2021 Brian Green
// Rust solution: 30 Nov 2023 Brian Green
//
// Problem 1: How many total square feet of wrapping paper should they order?
// Problem 2: How many total feet of ribbon should they order?
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

fn get_dimentions(boxes: &str) -> (u32, u32, u32) {
    let gift: Vec<&str> = boxes.split('x').collect();
    let length: u32 = gift[0].parse().unwrap();
    let width: u32 = gift[1].parse().unwrap();
    let height: u32 = gift[2].parse().unwrap();

    (length, width, height)
}

fn get_wrapping_paper(dimensions: &Vec<String>) -> u32 {
    let mut total_paper = 0;
    for boxes in dimensions {
        let (length, width, height) = get_dimentions(boxes);
        let surface: Vec<u32> = vec![2 * length * width, 2 * width * height, 2 * height * length];
        total_paper += surface.iter().sum::<u32>() + (surface.iter().min().unwrap() / 2);
    }
    total_paper
}

fn get_ribbon(dimensions: &Vec<String>) -> u32 {
    let mut total_ribbon = 0;
    for boxes in dimensions {
        let (length, width, height) = get_dimentions(boxes);
        let perimeter: Vec<u32> = vec![
            (2 * length) + (2 * width),
            (2 * width) + (2 * height),
            (2 * height) + (2 * length),
        ];
        total_ribbon += (length * width * height) + perimeter.iter().min().unwrap();
    }
    total_ribbon
}

fn main() -> std::io::Result<()> {
    let dimensions = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_wrapping_paper(&dimensions));
    // Part 2
    println!("Part 2 = {}", get_ribbon(&dimensions));
    Ok(())
}

/*
For example:

[Part 1]
A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of
wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of
wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

[Part 2]
A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap
the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap
the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
*/

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_wrapping_paper() {
        let test_data1 = vec!["2x3x4".to_string()];
        let test_data2 = vec!["1x1x10".to_string()];
        assert_eq!(get_wrapping_paper(&test_data1), 58);
        assert_eq!(get_wrapping_paper(&test_data2), 43);
    }

    #[test]
    fn test_get_ribbon() {
        let test_data1 = vec!["2x3x4".to_string()];
        let test_data2 = vec!["1x1x10".to_string()];
        assert_eq!(get_ribbon(&test_data1), 34);
        assert_eq!(get_ribbon(&test_data2), 14);
    }
}
