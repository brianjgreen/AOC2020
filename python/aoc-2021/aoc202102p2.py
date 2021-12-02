
# Advent of Code 2021 - Day 2 Part 1
# 2 Dec 2021 Brian Green
#
# Problem:
# What do you get if you multiply your final horizontal position by your final depth?
#

import os

filename = "data" + os.sep + "brian_aoc202102.dat"
with open(filename) as data_file:
    data_set = [dir.strip() for dir in data_file.readlines()]

aim = 0
depth = 0
position = 0

for dir in data_set:
    direction, movement = dir.split()
    moves = int(movement)

    if direction == "up":
        aim -= moves
    elif direction == "down":
        aim += moves
    elif direction == "forward":
        position += moves
        depth += moves * aim
    else:
        print(direction)

    if depth < 0:
        print("HELP!")

print(f"p={position} d={depth} t={position * depth}")
