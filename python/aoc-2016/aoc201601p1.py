#
# Advent of Code 2016 - Day 1 Part 1
# 1 Dec 2021 Brian Green
#
# Problem:
# How many blocks away is Easter Bunny HQ?
#

import os

filename = "data" + os.sep + "brian_aoc201601.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

directions = data_set[0].split(', ')

testcase1 = ['R2', 'L3']  # 5 blocks away.
testcase2 = ['R2', 'R2', 'R2']  # 2 blocks away.
testcase3 = ['R5', 'L5', 'R5', 'R3']  # 12 blocks away.

compass = {
    "north": {"x": 0, "y": 1, "L": "west", "R": "east"},
    "east": {"x": 1, "y": 0, "L": "north", "R": "south"},
    "south": {"x": 0, "y": -1, "L": "east", "R": "west"},
    "west": {"x": -1, "y": 0, "L": "south", "R": "north"}
}


def calc_distance(directions):
    distance = 0
    needle = 'north'
    x = 0
    y = 0
    for move in directions:
        needle = compass[needle][move[0]]
        steps = int(move[1:])
        x += steps * compass[needle]['x']
        y += steps * compass[needle]['y']

    return abs(x) + abs(y)


print(calc_distance(testcase1))
print(calc_distance(testcase2))
print(calc_distance(testcase3))
print(calc_distance(directions))
