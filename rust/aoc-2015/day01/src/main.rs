// Advent of Code 2015 - Day 1
// Python solution: 16 Nov 2021 Brian Green
// Rust solution: 29 Nov 2023 Brian Green
//
// Problem 1: To what floor do the instructions take Santa?
// Problem 2: What is the position of the character that causes Santa to first enter the basement?
pub(crate) use std::fs;

fn get_data() -> String {
    fs::read_to_string("data.dat").expect("Unable to read data file.")
}

fn get_floor_movement(movement: char) -> i32 {
    if movement == ')' {
        return -1;
    } else {
        return 1;
    }
}

fn find_floor(directions: &String) -> i32 {
    let mut floor = 0;
    for movement in directions.chars() {
        floor += get_floor_movement(movement);
    }
    floor
}

fn find_basement_position(directions: &String) -> i32 {
    let mut floor = 0;
    let mut position = 0;
    for movement in directions.chars() {
        position += 1;
        floor += get_floor_movement(movement);
        if floor == -1 {
            return position;
        }
    }
    println!("Unable to find basement!");
    0
}

fn main() -> std::io::Result<()> {
    let move_instr = get_data();
    // Part 1
    println!("Part 1 = {}", find_floor(&move_instr));
    // Part 2
    println!("Part 2 = {}", find_basement_position(&move_instr));
    Ok(())
}
