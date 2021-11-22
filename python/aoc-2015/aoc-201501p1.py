
# Advent of Code 2015 - Day 1 Part 1
# 16 Nov 2021 Brian Green
#
# Problem:
# To what floor do the instructions take Santa?
#

import os

filename = "data" + os.sep + "brian_aoc201501.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

floor = 0
for move in data_set[0]:
    if move == ")":
        floor -= 1
    else:
        floor += 1

print(floor)
