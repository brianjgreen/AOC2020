// Advent of Code 2023 - Day 4
// Rust solution: 4 Dec 2023 Brian Green
//
// Problem 1: How many points are they worth in total?
// Problem 2: How many total scratchcards do you end up with?
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

// Tally the score of winning numbers on a card
// Each matching number doubles the value of the prize
fn get_score(card: &String) -> i32 {
    // Need to optimize this code for parsing the cards in the data file.
    let card_format: Vec<&str> = card.split(":").collect();
    let numbers: Vec<&str> = card_format[1].split("|").collect();
    let winners: Vec<&str> = numbers[0].split(" ").collect();
    let my_picks: Vec<&str> = numbers[1].split(" ").collect();
    let mut final_score = 0;
    for win in winners.iter() {
        for my_num in my_picks.iter() {
            if win.len() == 0 || my_num.len() == 0 {
                // Need to optimize the code to deal with empty strings from parser
                continue;
            }
            if win == my_num {
                if final_score == 0 {
                    final_score = 1;
                } else {
                    final_score *= 2;
                }
            }
        }
    }
    return final_score;
}

// Sum all of the scores from each card
fn score_winners(cards: &Vec<String>) -> i32 {
    let mut total_score: i32 = 0;
    for scratch_card in cards {
        total_score += get_score(&scratch_card)
    }
    return total_score;
}

fn main() -> std::io::Result<()> {
    let cards = lines_from_file();
    // Part 1
    println!("Part 1 = {}", score_winners(&cards));
    // Part 2
    // println!("Part 2 = {}", power_of_cubes(&games));
    Ok(())
}
