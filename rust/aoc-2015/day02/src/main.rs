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
