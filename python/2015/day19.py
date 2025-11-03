# python day19.py ../../data/2015/day19.dat

import sys
import re


def parse_input(input_data):
    data_set = input_data.strip().split("\n")
    formula = data_set[-1]
    subs = {}
    for instruction in data_set:
        if "=>" in instruction:
            key, value = instruction.split(" => ")
            if key in subs:
                subs[key].append(value)
            else:
                subs[key] = [value]
    return formula, subs


def part1(formula, subs):
    new_formulas = []
    for key, values in subs.items():
        for match in re.finditer(key, formula):
            start, end = match.span()
            for val in values:
                new_formulas.append(formula[:start] + val + formula[end:])
    return len(set(new_formulas))


def part2(formula, subs):
    # This is a placeholder for part 2 solution
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = """H => HO
H => OH
O => HH
e => H
e => O

HOHOHO"""
    formula, subs = parse_input(input_data)
    print("Day 19 Part 1:", part1(formula, subs))
    print("Day 19 Part 2:", part2(formula, subs))
