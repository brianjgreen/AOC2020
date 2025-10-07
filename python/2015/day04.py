# python day04.py ../../data/2015/day04.dat

import hashlib
import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    """
    Find the lowest number that produces an MD5 hash with '00000'
    as the five leading characters.
    """
    base = 0
    while True:
        s = (
            data[0] + str(base)
        ).encode()  # Concatenate key and number, encode as bytes
        xhash = hashlib.md5(s).hexdigest()
        if xhash.startswith("00000"):
            return base
        base += 1

    return None


def part2(data):
    """
    Find the lowest number that produces an MD5 hash with '000000'
    as the six leading characters.
    """
    base = 0
    while True:
        s = (data[0] + str(base)).encode()
        xhash = hashlib.md5(s).hexdigest()
        if xhash.startswith("000000"):
            return base
        base += 1

    return None


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
abcdef
"""

    data = parse_input(input_data)
    print("Day 04 Part 1:", part1(data))
    print("Day 04 Part 2:", part2(data))
