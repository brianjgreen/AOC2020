#
# Advent of Code 2016 - Day 1 Part 2
# 1 Dec 2021 Brian Green
#
# Problem:
# How many blocks away is the first location you visit twice?
#

import os

filename = "data" + os.sep + "brian_aoc201601.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

directions = data_set[0].split(", ")

testcase1 = ["R8", "R4", "R4", "R8"]  # 4 blocks away.

compass = {
    "north": {"x": 0, "y": 1, "L": "west", "R": "east"},
    "east": {"x": 1, "y": 0, "L": "north", "R": "south"},
    "south": {"x": 0, "y": -1, "L": "east", "R": "west"},
    "west": {"x": -1, "y": 0, "L": "south", "R": "north"},
}


def calc_distance(directions):
    needle = "north"
    x = 0
    y = 0
    locations = []
    for move in directions:
        needle = compass[needle][move[0]]
        steps = int(move[1:])
        for s in range(steps):
            x += compass[needle]["x"]
            y += compass[needle]["y"]
            here = f"{x},{y}"
            if here in locations:
                return abs(x) + abs(y)
            else:
                locations.append(here)

    return 0


print(calc_distance(testcase1))
print(calc_distance(directions))
