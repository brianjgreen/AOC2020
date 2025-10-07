# python day10.py ../../data/2015/day10.dat

import sys
from itertools import groupby, islice

# NOTE: Used code from
# https://www.rosettacode.org/wiki/Look-and-say_sequence#Python


def lookandsay(number="1"):
    while True:
        yield number
        number = "".join(str(len(list(g))) + k for k, g in groupby(number))


def find_length(data, iterations):
    number = "\n".join(islice(lookandsay(data[0]), iterations + 1))
    one_number = number.split()
    return len(one_number[-1])


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    return find_length(data, 40)


def part2(data):
    return find_length(data, 50)


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
1
"""

    data = parse_input(input_data)
    print("Day 10 Part 1:", part1(data))
    print("Day 10 Part 2:", part2(data))
