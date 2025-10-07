# python day02.py ../../data/2015/day02.dat

import re
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
    grand_total = 0
    pattern = re.compile(r"(\d+)x(\d+)x(\d+)")
    for package in data:
        match = re.findall(pattern, package)
        if match:
            surface = []
            dimentions = [int(d) for d in match[0]]
            length = dimentions[0]
            width = dimentions[1]
            height = dimentions[2]
            surface.append(2 * length * width)
            surface.append(2 * width * height)
            surface.append(2 * height * length)
            total = sum(surface) + (min(surface) / 2)
            grand_total += total

    return int(grand_total)


def part2(data):
    """
    Solution for Part 2.
    """
    grand_total = 0
    pattern = re.compile(r"(\d+)x(\d+)x(\d+)")
    for package in data:
        match = re.findall(pattern, package)
        if match:
            perimeter = []
            dimentions = [int(d) for d in match[0]]
            length = dimentions[0]
            width = dimentions[1]
            height = dimentions[2]
            perimeter.append((2 * length) + (2 * width))
            perimeter.append((2 * width) + (2 * height))
            perimeter.append((2 * height) + (2 * length))
            total = (length * width * height) + min(perimeter)
            grand_total += total

    return grand_total


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
2x3x4
"""

    data = parse_input(input_data)
    print("Day 02 Part 1:", part1(data))
    print("Day 02 Part 2:", part2(data))
