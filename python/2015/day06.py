# python day06.py ../../data/2015/day06.dat

import re
import sys


def parse_input(input_data):
    """
    Parse the input data from the Advent of Code problem.
    Edit this function to fit the day's input format.
    """
    return input_data.strip().split("\n")


lights = {}


def turn_on(start_x, start_y, end_x, end_y, dir):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            lights[(x, y)] = dir


def turn_on_dimmer(start_x, start_y, end_x, end_y, dir):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            if (x, y) in lights:
                if dir < 0 and lights[(x, y)] < 1:
                    pass
                else:
                    lights[(x, y)] += dir
            else:
                if dir > 0:
                    lights[(x, y)] = dir


def toggle(start_x, start_y, end_x, end_y):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            if (x, y) in lights:
                if lights[(x, y)]:
                    lights[(x, y)] = False
                else:
                    lights[(x, y)] = True
            else:
                lights[(x, y)] = True


def part1(data):
    lights.clear()
    pattern = re.compile(r"(\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})")
    for instruction in data:
        coordinates = re.findall(pattern, instruction)[0]
        start_x, start_y, end_x, end_y = coordinates

        if "turn on" in instruction:
            turn_on(start_x, start_y, end_x, end_y, True)
        elif "turn off" in instruction:
            turn_on(start_x, start_y, end_x, end_y, False)
        else:
            toggle(start_x, start_y, end_x, end_y)

    lights_on = 0
    for bulb in lights:
        if lights[bulb]:
            lights_on += 1

    return lights_on


def part2(data):
    lights.clear()
    pattern = re.compile(r"(\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})")
    for instruction in data:
        coordinates = re.findall(pattern, instruction)[0]
        start_x, start_y, end_x, end_y = coordinates

        if "turn on" in instruction:
            turn_on_dimmer(start_x, start_y, end_x, end_y, 1)
        elif "turn off" in instruction:
            turn_on_dimmer(start_x, start_y, end_x, end_y, -1)
        else:
            turn_on_dimmer(start_x, start_y, end_x, end_y, 2)

    lights_on = 0
    for bulb in lights:
        lights_on += lights[bulb]

    return lights_on


if __name__ == "__main__":
    # Read input file or use test string
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        # Example test input, replace with actual test data
        input_data = """\
ugknbfddgicrmopn
"""

    data = parse_input(input_data)
    print("Day 06 Part 1:", part1(data))
    print("Day 06 Part 2:", part2(data))
