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

fn get_wrapping_paper(dimensions: &Vec<String>) -> u32 {
    let mut total_paper = 0;
    for boxes in dimensions {
        let gift: Vec<&str> = boxes.split("x").collect();
        let length: u32 = gift[0].parse().unwrap();
        let width: u32 = gift[1].parse().unwrap();
        let height: u32 = gift[2].parse().unwrap();
        let mut surface: Vec<u32> = Vec::new();
        surface.push(2 * length * width);
        surface.push(2 * width * height);
        surface.push(2 * height * length);
        total_paper += surface.iter().sum::<u32>() + (surface.iter().min().unwrap() / 2);
    }
    return total_paper;
}

fn get_ribbon(dimensions: &Vec<String>) -> u32 {
    let mut total_ribbon = 0;
    for boxes in dimensions {
        let gift: Vec<&str> = boxes.split("x").collect();
        let length: u32 = gift[0].parse().unwrap();
        let width: u32 = gift[1].parse().unwrap();
        let height: u32 = gift[2].parse().unwrap();
        let mut perimeter: Vec<u32> = Vec::new();
        perimeter.push((2 * length) + (2 * width));
        perimeter.push((2 * width) + (2 * height));
        perimeter.push((2 * height) + (2 * length));
        total_ribbon += (length * width * height) + perimeter.iter().min().unwrap();
    }
    return total_ribbon;
}

fn main() -> std::io::Result<()> {
    let dimensions = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_wrapping_paper(&dimensions));
    // Part 2
    println!("Part 2 = {}", get_ribbon(&dimensions));
    Ok(())
}
