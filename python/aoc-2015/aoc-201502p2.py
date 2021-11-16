
# Advent of Code 2015 - Day 2 Part 2
# 16 Nov 2021 Brian Green
#
# Problem:
#

import os
import re

filename = "data" + os.sep + "brian_aoc201502.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

grand_total = 0
pattern = re.compile("(\d+)x(\d+)x(\d+)")
for package in data_set:
    match = re.findall(pattern, package)
    if match:
        perimeter = []
        dimentions = [int(d) for d in match[0]]
        length = dimentions[0]
        width = dimentions[1]
        height = dimentions[2]
        perimeter.append((2 * length) + (2 * width))
        perimeter.append((2 * width) + (2 * height))
        perimeter.append((2 * height) + (2 * length))
        total = (length * width * height) + min(perimeter)
        print(
            f"{package} {match[0]} {total}")
        grand_total += total

print(grand_total)
