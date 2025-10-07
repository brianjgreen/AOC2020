# python day12.py ../../data/2015/day12.dat

import json
import re
import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def clear_dict(d):
    for i in d.values():
        if isinstance(i, dict):
            clear_dict(i)
        elif isinstance(i, list):
            get_red(i)
        elif "red" == i:
            d.clear()
            return True
    return False


def get_red(obj):
    for i in obj:
        if isinstance(i, dict):
            if clear_dict(i):
                continue
            get_red(i)
        elif isinstance(i, list):
            get_red(i)


def part1(data):
    pattern = re.compile(r"-{0,1}\d+")
    matches = re.findall(pattern, data[0])

    total = 0
    for i in matches:
        total += int(i)

    return total


def part2(data):
    data_json = json.loads(data[0])
    get_red(data_json)
    pattern = re.compile(r"-{0,1}\d+")
    matches = re.findall(pattern, str(data_json))

    total = 0
    for i in matches:
        total += int(i)

    return total


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
[1,2,3]
"""

    data = parse_input(input_data)
    print("Day 12 Part 1:", part1(data))
    print("Day 12 Part 2:", part2(data))
