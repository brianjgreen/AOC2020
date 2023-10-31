# Advent of Code 2021 - Day 2 Part 1
# 2 Dec 2021 Brian Green
#
# Problem:
# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?
#

import os

filename = "data" + os.sep + "brian_aoc202102.dat"
with open(filename) as data_file:
    data_set = [direction.strip() for direction in data_file.readlines()]

depth = 0
position = 0

for d in data_set:
    direction, movement = d.split()
    moves = int(movement)

    if direction == "up":
        depth -= moves
    elif direction == "down":
        depth += moves
    elif direction == "forward":
        position += moves
    else:
        print(direction)

    if depth < 0:
        print("HELP!")

print(f"p={position} d={depth} t={position * depth}")
