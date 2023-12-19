// Advent of Code 2023 - Day 19
// Rust solution: 19 Dec 2023 Brian Green
//
// Problem 1: what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?
// Problem 2: How many distinct combinations of ratings will be accepted by the Elves' workflows?
use std::collections::HashMap;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
};

// Return a Vector of Strings, each element is a String of a row of data
fn lines_from_file(filename: String) -> Vec<String> {
    let file = File::open(filename).expect("Unable to read data file.");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

// Execute the workflows until the part is accepted or rejected
fn process_part(
    x: i64,
    m: i64,
    a: i64,
    s: i64,
    curr_rule: &str,
    rules: HashMap<&str, &str>,
) -> bool {
    if curr_rule == "R" {
        // Reject part
        return false;
    } else if curr_rule == "A" {
        // Accept part
        return true;
    }
    let attrib: Vec<_> = rules.get(curr_rule).unwrap().split(',').collect();
    for test in attrib {
        if test == "R" {
            // Reject part
            return false;
        } else if test == "A" {
            // Accept part
            return true;
        } else {
            let cat = test.chars().next().unwrap();
            let lt_gt = test.chars().nth(1).unwrap();
            if lt_gt != '>' && lt_gt != '<' {
                // End of this workflow, go to next workflow
                return process_part(x, m, a, s, test, rules);
            }
            // If workflow matches a rule, execute the result (could be A, R, or next rule/workflow)
            let rule_format: Vec<_> = test.split(":").collect();
            let test_value: i64 = rule_format[0][2..rule_format[0].len()].parse().unwrap();
            let next_rule = rule_format[1];
            if lt_gt == '>' {
                if (cat == 'x' && x > test_value)
                    || (cat == 'm' && m > test_value)
                    || (cat == 'a' && a > test_value)
                    || (cat == 's' && s > test_value)
                {
                    return process_part(x, m, a, s, next_rule, rules);
                }
            } else {
                if (cat == 'x' && x < test_value)
                    || (cat == 'm' && m < test_value)
                    || (cat == 'a' && a < test_value)
                    || (cat == 's' && s < test_value)
                {
                    return process_part(x, m, a, s, next_rule, rules);
                }
            }
        }
    }
    println!("Rule failure! {}: {:?}", curr_rule, rules);
    false
}

// Start the workflow at rule "in"
fn accept_part(x: i64, m: i64, a: i64, s: i64, rules: HashMap<&str, &str>) -> bool {
    process_part(x, m, a, s, "in", rules)
}

// Extract the part numbers from the inventory
fn get_part_nums(part: &String) -> (i64, i64, i64, i64) {
    let mut x: i64 = 0;
    let mut m: i64 = 0;
    let mut a: i64 = 0;
    let mut s: i64 = 0;
    let cat: Vec<_> = part[1..part.len() - 1].split(',').collect();
    for rate in cat {
        let values: Vec<_> = rate.split('=').collect();
        let number: i64 = values[1].parse().unwrap();
        match values[0] {
            "x" => x = number,
            "m" => m = number,
            "a" => a = number,
            "s" => s = number,
            _ => println!("{} is not a category!", rate),
        }
    }
    (x, m, a, s)
}

// Extract the list of parts
fn get_parts(part_data: &Vec<String>) -> Vec<String> {
    let mut parts: Vec<String> = Vec::new();
    for data in part_data {
        if data.len() > 0 && data.chars().next().unwrap() == '{' {
            parts.push(data.to_string());
        }
    }
    parts
}

// Extract the list of rules (or workflows)
fn get_rules(part_data: &Vec<String>) -> HashMap<&str, &str> {
    let mut rules: HashMap<&str, &str> = HashMap::new();
    for data in part_data {
        if data.len() > 0 && data.chars().next().unwrap() != '{' {
            let rule_format: Vec<_> = data[0..data.len() - 1].split('{').collect();
            rules.insert(rule_format[0], rule_format[1]);
        }
    }
    rules
}

// Get parts and rules, execute the workflow rules on each part, sum the category numbers for accepted parts
// For part 1
fn sum_of_parts(part_data: &Vec<String>) -> i64 {
    let mut sum_results: i64 = 0;
    let all_parts = get_parts(part_data);
    let all_rules = get_rules(part_data);
    for part in all_parts {
        let (x, m, a, s) = get_part_nums(&part);
        if accept_part(x, m, a, s, all_rules.clone()) {
            sum_results += x + m + a + s;
        }
    }
    sum_results
}

// Need to rework this brute force for part 2
// Find all combinations of x, m, a, and s that are accepted parts
fn find_all_good_parts(part_data: &Vec<String>) -> i64 {
    let mut sum_results: i64 = 0;
    let all_rules = get_rules(part_data);
    for x in 1..4001 {
        for m in 1..4001 {
            println!("{}", m);
            for a in 1..4001 {
                for s in 1..4001 {
                    if accept_part(x, m, a, s, all_rules.clone()) {
                        sum_results += 1;
                    }
                }
            }
        }
    }
    sum_results
}

fn main() -> std::io::Result<()> {
    let part_data = lines_from_file("data.dat".to_string());
    // Part 1
    println!("Part 1 = {}", sum_of_parts(&part_data));
    // Part 2
    println!("Part 2 = {}", find_all_good_parts(&part_data));
    Ok(())
}
