// Advent of Code 2015 - Day 3
// Python solution: 17 Nov 2021 Brian Green
// Rust solution: 30 Nov 2023 Brian Green
//
// Problem 1: How many houses receive at least one present? (one Santa)
// Problem 2: How many houses receive at least one present? (twp Santas)
use std::collections::HashMap;
pub(crate) use std::fs;

fn get_data() -> String {
    fs::read_to_string("data.dat").expect("Unable to read data file.")
}

fn get_num_houses(directions: &String) -> usize {
    let mut houses = HashMap::from([((0, 0), 1)]);
    let mut x = 0;
    let mut y = 0;
    for dir in directions.chars() {
        match dir {
            '^' => y += 1,
            '>' => x += 1,
            '<' => x -= 1,
            'v' => y -= 1,
            _ => println!("Unknown direction {}", dir),
        }
        let count = houses.entry((x, y)).or_insert(0);
        *count += 1;
    }
    return houses.keys().len();
}

fn get_num_houses_two_santas(directions: &String) -> usize {
    let mut houses = HashMap::from([((0, 0), 2)]);
    let mut santa = true;
    let mut santa_x = 0;
    let mut santa_y = 0;
    let mut robo_x = 0;
    let mut robo_y = 0;
    for dir in directions.chars() {
        let mut delta_y = 0;
        let mut delta_x = 0;
        match dir {
            '^' => delta_y = 1,
            '>' => delta_x = 1,
            '<' => delta_x = -1,
            'v' => delta_y = -1,
            _ => println!("Unknown direction {}", dir),
        }
        if santa {
            santa = false;
            santa_x += delta_x;
            santa_y += delta_y;
            let count = houses.entry((santa_x, santa_y)).or_insert(0);
            *count += 1;
        } else {
            santa = true;
            robo_x += delta_x;
            robo_y += delta_y;
            let count = houses.entry((robo_x, robo_y)).or_insert(0);
            *count += 1;
        }
    }
    return houses.keys().len();
}

fn main() -> std::io::Result<()> {
    let move_instr = get_data();
    // Part 1
    println!("Part 1 = {}", get_num_houses(&move_instr));
    // Part 2
    println!("Part 2 = {}", get_num_houses_two_santas(&move_instr));
    Ok(())
}
