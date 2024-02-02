// Advent of Code 2023 - Day 2
// Rust solution: 2 Dec 2023 Brian Green
//
// Problem 1: What is the sum of the IDs of those games?
// Problem 2: What is the sum of the power of these sets?
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

// Return the Game id number from the gaming session
fn get_game_id(game_play: &str) -> i32 {
    let game_format: Vec<&str> = game_play.split(':').collect();
    let game_header: Vec<&str> = game_format[0].split(' ').collect();
    let game_id: i32 = game_header[1].parse().unwrap();
    game_id
}

// Calculate the minimum number of dice needed to play each game
fn min_cubes_needed(game: &str) -> (i32, i32, i32) {
    let mut red: i32 = 0;
    let mut green: i32 = 0;
    let mut blue: i32 = 0;
    let dice: Vec<&str> = game.split(',').collect();
    for die in dice {
        let parts: Vec<&str> = die.split(' ').collect();
        let number_of_die: i32 = parts[1].parse().unwrap();
        if die.contains("red") {
            red += number_of_die;
        } else if die.contains("green") {
            green += number_of_die;
        } else if die.contains("blue") {
            blue += number_of_die;
        }
    }
    (red, green, blue)
}

// only 12 red cubes, 13 green cubes, and 14 blue cubes
fn is_cheating(game: &str) -> bool {
    let max_red: i32 = 12;
    let max_green: i32 = 13;
    let max_blue: i32 = 14;
    let (red, green, blue) = min_cubes_needed(game);
    if red > max_red || blue > max_blue || green > max_green {
        return true;
    }
    false
}

// Returns true if the game was played with the available dice quantities
fn is_game_possible(game_play: &str) -> bool {
    let game_format: Vec<&str> = game_play.split(':').collect();
    let game_sets: Vec<&str> = game_format[1].split(';').collect();
    for game in game_sets {
        if is_cheating(game) {
            return false;
        }
    }
    true
}

// Return a sum of all possible games given the number of dice available
fn sum_possible_games(games: &Vec<String>) -> i32 {
    let mut total_ids: i32 = 0;
    for game_play in games {
        let game_id = get_game_id(game_play);
        if is_game_possible(game_play) {
            total_ids += game_id
        }
    }
    total_ids
}

// Return the power which is the minimum necessary dice for each color multiplied together
fn get_power(game_play: &str) -> i32 {
    let mut max_red: i32 = 0;
    let mut max_green: i32 = 0;
    let mut max_blue: i32 = 0;
    let game_format: Vec<&str> = game_play.split(':').collect();
    let game_sets: Vec<&str> = game_format[1].split(';').collect();
    for game in game_sets {
        let (red, green, blue) = min_cubes_needed(game);
        if red > max_red {
            max_red = red;
        }
        if green > max_green {
            max_green = green;
        }
        if blue > max_blue {
            max_blue = blue;
        }
    }
    max_red * max_green * max_blue
}

// Sum all of the powers from each game
fn power_of_cubes(games: &Vec<String>) -> i32 {
    let mut total_power: i32 = 0;
    for game_play in games {
        total_power += get_power(game_play)
    }
    total_power
}

fn main() -> std::io::Result<()> {
    let games = lines_from_file();
    // Part 1
    println!("Part 1 = {}", sum_possible_games(&games));
    // Part 2
    println!("Part 2 = {}", power_of_cubes(&games));
    Ok(())
}
