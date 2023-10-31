# Advent of Code 2015 - Day 1 Part 2
# 16 Nov 2021 Brian Green
#
# Problem:
# What is the position of the character that causes Santa to first enter the basement?
#

import os

filename = "data" + os.sep + "brian_aoc201501.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

floor = 0
position = 0
for move in data_set[0]:
    position += 1
    if move == ")":
        floor -= 1
    else:
        floor += 1
    if floor == -1:
        print(f"BASEMENT pos={position}")

print(floor)
