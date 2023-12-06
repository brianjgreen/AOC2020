// Advent of Code 2023 - Day 5
// Rust solution: 5 Dec 2023 Brian Green
//
// Problem 1: What is the lowest location number that corresponds to any of the initial seed numbers list?
// Problem 2: What is the lowest location number that corresponds to any of the initial seed numbers range?
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

fn get_seeds(almanac: &Vec<String>) -> Vec<u64> {
    let seed_header: Vec<&str> = almanac[0].split(": ").collect();
    let seeds: Vec<u64> = seed_header[1]
        .split(" ")
        .map(|x| x.parse::<u64>().unwrap())
        .collect();
    seeds
}

fn low_seed_loc(almanac: &Vec<String>, seeds: Vec<u64>) -> u64 {
    // let seeds = get_seeds(almanac);
    let mut min_location: u64 = 0;
    for init_seed in seeds {
        let mut seed_location = init_seed;
        let mut soil_found: bool = false;
        for soil in almanac {
            if soil.contains(" map:") {
                soil_found = false;
            }
            if !soil_found && !soil.contains(" map:") && !soil.contains("seeds") && soil.len() > 0 {
                let dest_sour_rang: Vec<u64> =
                    soil.split(" ").map(|x| x.parse::<u64>().unwrap()).collect();
                let dest = dest_sour_rang[0];
                let source = dest_sour_rang[1];
                let seed_range = dest_sour_rang[2];

                if seed_location >= source && seed_location < source + seed_range {
                    soil_found = true;
                    seed_location = dest + (seed_location - source);
                }
            }
        }
        if min_location == 0 || seed_location < min_location {
            min_location = seed_location;
        }
    }
    min_location
}

fn get_min_loc_seed_list(almanac: &Vec<String>) -> u64 {
    low_seed_loc(&almanac, get_seeds(almanac))
}

fn get_min_loc_seed_range(almanac: &Vec<String>) -> u64 {
    let seed_header: Vec<&str> = almanac[0].split(": ").collect();
    let seed_ranges: Vec<u64> = seed_header[1]
        .split(" ")
        .map(|x| x.parse::<u64>().unwrap())
        .collect();
    let mut location: u64 = 0;
    loop {
        let mut seed_line: i32 = (almanac.len() - 1).try_into().unwrap();
        let mut map_line = almanac.len();
        let mut seed_location = location;
        let mut soil_found: bool = false;
        while seed_line >= 0 { 
            map_line -= 1;
            let soil = &almanac[map_line];
            if soil.contains(" map:") {
                soil_found = false;
            }
            if !soil_found && !soil.contains(" map:") && !soil.contains("seeds") && soil.len() > 0 {
                let dest_sour_rang: Vec<u64> =
                    soil.split(" ").map(|x| x.parse::<u64>().unwrap()).collect();
                let dest = dest_sour_rang[0];
                let source = dest_sour_rang[1];
                let seed_range = dest_sour_rang[2];

                if seed_location >= dest && seed_location < dest + seed_range {
                    soil_found = true;
                    seed_location = source + (seed_location - dest);
                }
            }
            seed_line -= 1;
        }
        let mut i = 0;
        while i < seed_ranges.len() {
            if seed_location >= seed_ranges[i] && seed_location < seed_ranges[i] + seed_ranges[i+1] {
                return location;
            }
            i += 2;
        }
        location += 1;
        if location % 100000 == 0 {
            println!("loc={}", location)
        }
    }
    /*
    for init_seed in seeds {
        let mut seed_location = init_seed;
        let mut soil_found: bool = false;
        for soil in almanac {
            if soil.contains(" map:") {
                soil_found = false;
            }
            if !soil_found && !soil.contains(" map:") && !soil.contains("seeds") && soil.len() > 0 {
                let dest_sour_rang: Vec<u64> =
                    soil.split(" ").map(|x| x.parse::<u64>().unwrap()).collect();
                let dest = dest_sour_rang[0];
                let source = dest_sour_rang[1];
                let seed_range = dest_sour_rang[2];

                if seed_location >= source && seed_location < source + seed_range {
                    soil_found = true;
                    seed_location = dest + (seed_location - source);
                }
            }
        }
        if min_location == 0 || seed_location < min_location {
            min_location = seed_location;
        }
    }
    min_location*/
    /*
    let seed_header: Vec<&str> = almanac[0].split(": ").collect();
    let seed_ranges: Vec<u64> = seed_header[1]
        .split(" ")
        .map(|x| x.parse::<u64>().unwrap())
        .collect();
    let mut i = 0;
    while i < seed_ranges.len() {
        let s_range: u64 = seed_ranges[i] + seed_ranges[i + 1];
        let more_seeds: Vec<u64> = (seed_ranges[i]..s_range).collect();
        println!("Seeds generated");
        println!("{}", low_seed_loc(&almanac, more_seeds));
        i += 2;
    }*/
    //0
}

fn main() -> std::io::Result<()> {
    let almanac = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_min_loc_seed_list(&almanac));
    // Part 2
    println!("Part 2 = {}", get_min_loc_seed_range(&almanac));
    Ok(())
}
