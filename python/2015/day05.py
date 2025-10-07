# python day05.py ../../data/2015/day05.dat

import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


def part1(data):
    nice = 0

    for message in data:
        # at least three vowels
        vowels = 0
        for letter in "aeiou":
            vowels += message.count(letter)
        if vowels < 3:
            continue

        # at least one letter appears twice in a row
        doubles = [i + j for i, j in zip(message, message[1:]) if i == j]
        if len(doubles) == 0:
            continue

        # does not contain the strings ab, cd, pq, or xy
        if any(sub in message for sub in ("ab", "cd", "pq", "xy")):
            continue

        nice += 1

    return nice


def part2(data):
    nice = 0

    for message in data:
        # a pair of any two letters that appears at least twice
        # in the string without overlapping
        pair = message[:2]
        remain = message[2:].strip()
        count = 0
        while len(remain) > 1:
            if pair in remain:
                count += 1
            pair = pair[1] + remain[0]
            remain = remain[1:]

        if count == 0:
            continue

        # at least one letter which repeats
        # with exactly one letter between them
        double_gap = [i + j for i, j in zip(message, message[2:]) if i == j]
        if len(double_gap) == 0:
            continue

        nice += 1

    return nice


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
"""

    data = parse_input(input_data)
    print("Day 05 Part 1:", part1(data))
    print("Day 05 Part 2:", part2(data))
