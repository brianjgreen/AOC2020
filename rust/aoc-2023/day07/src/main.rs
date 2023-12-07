// Advent of Code 2023 - Day 7
// Rust solution: 7 Dec 2023 Brian Green
//
// Problem 1: What are the total winnings??
// Problem 2: ?
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

// https://stackoverflow.com/questions/36971516/how-can-i-convert-a-collection-of-values-into-a-hashmap-that-counts-them
// Return a HashMap of character frequencies in a string
fn str_char_freq(word: &str) -> HashMap<char, i32> {
    word.chars().fold(HashMap::new(), |mut acc, c| {
        *acc.entry(c).or_insert(0) += 1;
        acc
    })
}

// Every hand is exactly one type. From strongest to weakest, they are:
// 6 - Five of a kind, where all five cards have the same label: AAAAA
// 5 - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
// 4 - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
// 3 - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
// 2 - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
// 1 - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
// 0 - High card, where all cards' labels are distinct: 23456
fn get_hand_type(hand: &str) -> u64 {
    let card_freq = str_char_freq(hand);
    let mut hand_type: u64 = 0;
    let distro: Vec<_> = card_freq.values().collect();
    // Need to optmize the checking of the values
    // Not sure that &&num[x] is the correct way to do this
    let num: Vec<i32> = vec![0, 1, 2, 3, 4, 5];
    if distro.contains(&&num[5]) {
        println!("{} is 5 of a kind!", hand);
        hand_type = 6;
    } else if distro.contains(&&num[4]) {
        println!("{} is 4 of a kind!", hand);
        hand_type = 5;
    } else if distro.contains(&&num[3]) && distro.contains(&&num[2]) {
        println!("{} is a full house!", hand);
        hand_type = 4;
    } else if distro.contains(&&num[3]) {
        println!("{} is a three of a kind!", hand);
        hand_type = 3;
    } else if distro.contains(&&num[2]) {
        if distro.iter().filter(|&n| *n == &num[2]).count() == 2 {
            println!("{} is two pairs.", hand);
            hand_type = 2;
        } else {
            println!("{} is a pair.", hand);
            hand_type = 1;
        }
    } else {
        println!("{} is high card only.", hand);
    }
    hand_type
}

fn get_hands_with_bids(hands: &Vec<String>) -> HashMap<&str, u64> {
    let mut hands_bids: HashMap<&str, u64> = HashMap::new();
    for hand_bid in hands {
        let hand_bid_format: Vec<&str> = hand_bid.split(" ").collect();
        let hand = hand_bid_format[0];
        let bid: u64 = hand_bid_format[1].parse().unwrap();
        hands_bids.insert(hand, bid);
    }
    hands_bids
}

fn get_total_winnings(hands: &Vec<String>) -> u64 {
    // println!("{:?}", hands);
    let mut counter: u64 = 0;
    let hands_bids = get_hands_with_bids(hands);
    for hand in hands_bids.keys() {
        counter += get_hand_type(*hand);
    }
    counter
}

fn main() -> std::io::Result<()> {
    let hands = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_total_winnings(&hands));
    // Part 2
    // println!("Part 2 = {}", num_of_scratch_tickets(&cards));
    Ok(())
}
