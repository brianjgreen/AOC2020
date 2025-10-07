# python day03.py ../../data/2015/day03.dat

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
    houses = {(0, 0): 1}
    x = 0
    y = 0

    for direction in data[0]:
        if direction == "^":
            y += 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        else:
            y -= 1

        if (x, y) in houses:
            houses[(x, y)] += 1
        else:
            houses[(x, y)] = 1

    return int(len(houses))


def part2(data):
    """
    Solution for Part 2.
    """
    houses = {(0, 0): 1}
    dalek = {}
    x = 0
    y = 0
    dalek_x = 0
    dalek_y = 0

    santa = True

    for direction in data[0]:
        if direction == "^":
            if santa:
                y += 1
            else:
                dalek_y += 1
        elif direction == ">":
            if santa:
                x += 1
            else:
                dalek_x += 1
        elif direction == "<":
            if santa:
                x -= 1
            else:
                dalek_x -= 1
        else:
            if santa:
                y -= 1
            else:
                dalek_y -= 1

        if santa:
            santa = False
            if (x, y) in houses:
                houses[(x, y)] += 1
            else:
                if (x, y) not in dalek:
                    houses[(x, y)] = 1
        else:
            santa = True
            if (dalek_x, dalek_y) in dalek:
                dalek[(dalek_x, dalek_y)] += 1
            else:
                if (dalek_x, dalek_y) not in houses:
                    dalek[(dalek_x, dalek_y)] = 1

    total = len(houses) + len(dalek)

    return total


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
^v^v^v^v^v
"""

    data = parse_input(input_data)
    print("Day 03 Part 1:", part1(data))
    print("Day 03 Part 2:", part2(data))
