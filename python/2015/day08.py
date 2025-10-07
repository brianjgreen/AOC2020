# python day08.py ../../data/2015/day08.dat

import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    total = 0
    memory = 0

    for item in data:
        mess = item.strip()[1:-1]
        total += len(mess) + 2
        chars = list(mess)
        while len(chars) > 0:
            c = chars.pop(0)
            if c == "\\":
                d = chars.pop(0)
                if d == "\\" or d == '"':
                    pass
                elif d == "x":
                    chars.pop(0)
                    chars.pop(0)
            memory += 1

    return total - memory


def part2(data):
    total = 0
    enc_total = 0
    memory = 0

    for item in data:
        mess = item.strip()[1:-1]
        total += len(mess) + 2
        enc_total += len(mess) + 6
        chars = list(mess)
        while len(chars) > 0:
            c = chars.pop(0)
            if c == "\\":
                enc_total += 1
                d = chars.pop(0)
                if d == "\\" or d == '"':
                    enc_total += 1
                elif d == "x":
                    chars.pop(0)
                    chars.pop(0)
            memory += 1

    return enc_total - total


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
""
"abc"
"aaa\"aaa"
"\x27"
"""

    data = parse_input(input_data)
    print("Day 08 Part 1:", part1(data))
    print("Day 08 Part 2:", part2(data))
