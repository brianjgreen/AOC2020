# python day16.py ../../data/2015/day16.dat

import sys


def parse_input(input_data):
    aunts = {}
    for sue in input_data.strip().split("\n"):
        attribs = sue.split()
        aunts[attribs[1][:-1]] = {
            attribs[2][:-1]: int(attribs[3][:-1]),
            attribs[4][:-1]: int(attribs[5][:-1]),
            attribs[6][:-1]: int(attribs[7]),
        }
    return aunts


def part1(aunts):
    matching_aunt = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    eligible_aunts = []
    for sue in aunts:
        i = 0
        for k, v in aunts[sue].items():
            if v == matching_aunt[k]:
                i += 1
        if i == 3:
            eligible_aunts.append(sue)
    return eligible_aunts


def part2(aunts):
    matching_aunt = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    eligible_aunts = []
    for sue in aunts:
        i = 0
        for k, v in aunts[sue].items():
            if k == "cats" or k == "trees":
                if v > matching_aunt[k]:
                    i += 1
            elif k == "pomeranians" or k == "goldfish":
                if v < matching_aunt[k]:
                    i += 1
            else:
                if v == matching_aunt[k]:
                    i += 1
        if i == 3:
            eligible_aunts.append(sue)
    return eligible_aunts


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = """Sue 1: children: 3, cats: 7, samoyeds: 2
Sue 2: children: 3, cats: 7, samoyeds: 2
Sue 3: children: 3, cats: 7, samoyeds: 2
"""
    aunts = parse_input(input_data)
    print("Day 16 Part 1:", part1(aunts))
    print("Day 16 Part 2:", part2(aunts))
