// Advent of Code 2023 - Day 4
// Rust solution: 4 Dec 2023 Brian Green
//
// Problem 1: How many points are they worth in total?
// Problem 2: How many total scratchcards do you end up with?
use std::collections::HashMap;
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

// Return the winning numbers and the players numbers
fn get_winners_players(card: &str) -> (Vec<&str>, Vec<&str>) {
    // Need to optimize this code for parsing the cards in the data file.
    let card_format: Vec<&str> = card.split(':').collect();
    let numbers: Vec<&str> = card_format[1].split('|').collect();
    let winners: Vec<&str> = numbers[0].split(' ').collect();
    let my_picks: Vec<&str> = numbers[1].split(' ').collect();
    (winners, my_picks)
}

// Tally the score of winning numbers on a card
// Each matching number doubles the value of the prize
fn get_score(card: &str) -> i32 {
    let mut final_score = 0;
    let (winners, my_picks) = get_winners_players(card);
    for win in winners.iter() {
        for my_num in my_picks.iter() {
            if win.is_empty() || my_num.is_empty() {
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
    final_score
}

// Return the number of winning player numbers on a card
fn get_winners(card: &str) -> i32 {
    let mut num_of_winners = 0;
    let (winners, my_picks) = get_winners_players(card);
    for win in winners.iter() {
        for my_num in my_picks.iter() {
            if win.is_empty() || my_num.is_empty() {
                // Need to optimize the code to deal with empty strings from parser
                continue;
            }
            if win == my_num {
                num_of_winners += 1;
            }
        }
    }
    num_of_winners
}

// Sum all of the scores from each card
fn score_winners(cards: &Vec<String>) -> i32 {
    let mut total_score: i32 = 0;
    for scratch_card in cards {
        total_score += get_score(scratch_card)
    }
    total_score
}

fn num_of_scratch_tickets(cards: &Vec<String>) -> i32 {
    // let mut total_cards: i32 = 0;
    let mut cloned_cards: HashMap<i32, i32> = HashMap::new();
    let mut total_cards: HashMap<i32, i32> = HashMap::new();
    let mut i: i32 = 1;
    for scratch_card in cards {
        // count each original card
        total_cards.insert(i, 1);
        // Add the number of winning payer numbers to each card
        // This will be the number of subsequent cards to clone
        let count = cloned_cards.entry(i).or_insert(0);
        *count += get_winners(scratch_card);
        i += 1;
    }
    for card in 1..i {
        // Clone a number of subsequent cards equal to the number of winning player numbers
        let mut num_win = cloned_cards[&card];
        while num_win != 0 {
            // Repeat the cloning for all clones of the original card
            let next_card = card + num_win;
            *total_cards.get_mut(&next_card).unwrap() += total_cards[&card];
            num_win -= 1;
        }
    }
    total_cards.values().sum()
}

fn main() -> std::io::Result<()> {
    let cards = lines_from_file();
    // Part 1
    println!("Part 1 = {}", score_winners(&cards));
    // Part 2
    println!("Part 2 = {}", num_of_scratch_tickets(&cards));
    Ok(())
}
