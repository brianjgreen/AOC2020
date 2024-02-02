// Advent of Code 2023 - Day 7
// Rust solution: 7 Dec 2023 Brian Green
//
// Problem 1: What are the total winnings?
// Problem 2: What are the new total winnings? (Joker rules)
use std::collections::HashMap;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

// Types of Hands ordered by strength (highest to lowest)
enum HandType {
    FiveOfAKind,
    FourOfAKind,
    FullHouse,
    ThreeOfAKind,
    TwoPair,
    OnePair,
    HighCard,
}

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

// Convert the cards into alphabetic order so their values can be sorted
fn get_card_value(hand: &str, part2: bool) -> String {
    let mut card_to_alpha = HashMap::from([
        ('A', 'a'),
        ('K', 'b'),
        ('Q', 'c'),
        ('J', 'd'),
        ('T', 'e'),
        ('9', 'f'),
        ('8', 'g'),
        ('7', 'h'),
        ('6', 'i'),
        ('5', 'j'),
        ('4', 'k'),
        ('3', 'l'),
        ('2', 'm'),
    ]);
    if part2 {
        card_to_alpha.remove(&'J');
        card_to_alpha.insert('J', 'n');
    }
    let mut alpha_hand: String = String::new();
    for c in hand.chars() {
        alpha_hand.push(*card_to_alpha.get(&c).unwrap());
    }
    alpha_hand
}

// Every hand is exactly one type. From strongest to weakest, they are:
// Five of a kind, where all five cards have the same label: AAAAA
// Four of a kind, where four cards have the same label and one card has a different label: AA8AA
// Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
// Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
// Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
// One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
// High card, where all cards' labels are distinct: 23456
fn get_hand_type(hand: &str, part2: bool) -> HandType {
    let mut card_freq = str_char_freq(hand);
    let mut jokers = 0;
    if part2 && card_freq.get(&'n').is_some() {
        jokers = *card_freq.get(&'n').unwrap();
        card_freq.remove(&'n');
        if jokers == 5 {
            return HandType::FiveOfAKind;
        }
    }
    let distro: Vec<_> = card_freq.values().collect();
    // Need to optmize the checking of the values
    // Not sure that &&num[x] is the correct way to do this
    let num: Vec<i32> = vec![0, 1, 2, 3, 4, 5];
    if distro.contains(&&num[5]) {
        HandType::FiveOfAKind
    } else if distro.contains(&&num[4]) {
        if jokers == 1 {
            return HandType::FiveOfAKind;
        }
        return HandType::FourOfAKind;
    } else if distro.contains(&&num[3]) && distro.contains(&&num[2]) {
        return HandType::FullHouse;
    } else if distro.contains(&&num[3]) {
        match jokers {
            1 => return HandType::FourOfAKind,
            2 => return HandType::FiveOfAKind,
            _ => return HandType::ThreeOfAKind,
        }
    } else if distro.contains(&&num[2]) {
        if distro.iter().filter(|&n| *n == &num[2]).count() == 2 {
            if jokers == 1 {
                return HandType::FullHouse;
            }
            return HandType::TwoPair;
        } else {
            match jokers {
                1 => return HandType::ThreeOfAKind,
                2 => return HandType::FourOfAKind,
                3 => return HandType::FiveOfAKind,
                _ => return HandType::OnePair,
            }
        }
    } else {
        match jokers {
            1 => return HandType::OnePair,
            2 => return HandType::ThreeOfAKind,
            3 => return HandType::FourOfAKind,
            4 => return HandType::FiveOfAKind,
            _ => return HandType::HighCard,
        }
    }
}

// Parse the data file into a HashMap of hand with bid
fn get_hands_with_bids(hands: &Vec<String>, part2: bool) -> HashMap<String, u64> {
    let mut hands_bids: HashMap<String, u64> = HashMap::new();
    for hand_bid in hands {
        let hand_bid_format: Vec<&str> = hand_bid.split(' ').collect();
        let hand = get_card_value(hand_bid_format[0], part2);
        let bid: u64 = hand_bid_format[1].parse().unwrap();
        hands_bids.insert(hand, bid);
    }
    hands_bids
}

// Sort the hands into hand types then sort by value low to high
// Return the sum the products from lowest value to highest multiplied by enumerator
fn get_total_winnings(hands: &Vec<String>, part2: bool) -> u64 {
    let mut counter: u64 = 0;
    let hands_bids = get_hands_with_bids(hands, part2);
    let mut five_of_a_kind: Vec<&str> = Vec::new();
    let mut four_of_a_kind: Vec<&str> = Vec::new();
    let mut full_house: Vec<&str> = Vec::new();
    let mut three_of_a_kind: Vec<&str> = Vec::new();
    let mut two_pair: Vec<&str> = Vec::new();
    let mut one_pair: Vec<&str> = Vec::new();
    let mut high_card: Vec<&str> = Vec::new();

    for hand in hands_bids.keys() {
        match get_hand_type(hand, part2) {
            HandType::FiveOfAKind => five_of_a_kind.push(hand),
            HandType::FourOfAKind => four_of_a_kind.push(hand),
            HandType::FullHouse => full_house.push(hand),
            HandType::ThreeOfAKind => three_of_a_kind.push(hand),
            HandType::TwoPair => two_pair.push(hand),
            HandType::OnePair => one_pair.push(hand),
            HandType::HighCard => high_card.push(hand),
        }
    }
    five_of_a_kind.sort();
    five_of_a_kind.reverse();
    four_of_a_kind.sort();
    four_of_a_kind.reverse();
    full_house.sort();
    full_house.reverse();
    three_of_a_kind.sort();
    three_of_a_kind.reverse();
    two_pair.sort();
    two_pair.reverse();
    one_pair.sort();
    one_pair.reverse();
    high_card.sort();
    high_card.reverse();

    let mut i: u64 = 1;
    for cards in high_card {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    for cards in one_pair {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    for cards in two_pair {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    for cards in three_of_a_kind {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    for cards in full_house {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    for cards in four_of_a_kind {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    for cards in five_of_a_kind {
        counter += i * hands_bids.get(cards).unwrap();
        i += 1;
    }
    counter
}

fn main() -> std::io::Result<()> {
    let hands = lines_from_file();
    // Part 1
    println!("Part 1 = {}", get_total_winnings(&hands, false));
    // Part 2
    println!("Part 2 = {}", get_total_winnings(&hands, true));
    Ok(())
}
