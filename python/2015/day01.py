# python day01.py ../../data/2015/day01.dat

import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    """
    Solution for Part 1.
    """
    floor = 0
    for move in data[0]:
        if move == ")":
            floor -= 1
        else:
            floor += 1

    return floor


def part2(data):
    """
    Solution for Part 2.
    """
    floor = 0
    position = 0
    for move in data[0]:
        position += 1
        if move == ")":
            floor -= 1
        else:
            floor += 1
        if floor == -1:
            return position

    return None


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
))(((((
"""

    data = parse_input(input_data)
    print("Day 01 Part 1:", part1(data))
    print("Day 01 Part 2:", part2(data))
