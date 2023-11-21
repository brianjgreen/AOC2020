# Advent of Code 2021 - Day 14 Part 1
# 21 Nov 2023 Brian Green
#
# Problem: What do you get if you take the quantity of the most common element
# and subtract the quantity of the least common element?
#

import collections
import os


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data" + os.sep + "brian_aoc202114.dat"
    with open(filename) as data_file:
        data_set = [pos.strip() for pos in data_file.readlines()]

    return data_set


def get_template(raw_data):
    """Return the first element of the raw_data which is the template"""
    return raw_data[0]


def get_polymer_rules(raw_data):
    """Return a dictionary of polymer rules from the raw data"""
    polymer_rules = {}
    for rule in raw_data:
        if " -> " in rule:
            key, data = rule.split(" -> ")
            polymer_rules[key] = data

    return polymer_rules


def insert_pairs(polymer, rules):
    """Return a new polymer string after inserting the pairs as per the paring rules"""
    new_polymer = ""
    for element in range(len(polymer)):
        new_polymer += polymer[element]
        if element == len(polymer) - 1:
            pass
        else:
            pair = polymer[element] + polymer[element + 1]
            if pair in rules:
                new_polymer += rules[pair]
    return new_polymer


if __name__ == "__main__":
    raw_data = get_data()
    polymer = get_template(raw_data)
    rules = get_polymer_rules(raw_data)
    print(polymer)
    for pairing_iter in range(10):
        print(f"iteration = {pairing_iter}")
        polymer = insert_pairs(polymer, rules)

    count = collections.Counter(polymer)
    most_common = count.most_common(1)[0][1]
    print(f"most common char freq = {most_common}")
    least_common_char = min(count, key=count.get)
    least_common = polymer.count(least_common_char)
    print(f"least common char freq = {least_common}")
    print(most_common - least_common)
