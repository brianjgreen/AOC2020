
# Advent of Code 2015 - Day 2 Part 1
# 16 Nov 2021 Brian Green
#
# Problem:
# How many total square feet of wrapping paper should they order?
#

import os
import re

filename = "data" + os.sep + "brian_aoc201502.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

grand_total = 0
pattern = re.compile(r"(\d+)x(\d+)x(\d+)")
for package in data_set:
    match = re.findall(pattern, package)
    if match:
        surface = []
        dimentions = [int(d) for d in match[0]]
        length = dimentions[0]
        width = dimentions[1]
        height = dimentions[2]
        surface.append(2 * length * width)
        surface.append(2 * width * height)
        surface.append(2 * height * length)
        total = sum(surface) + (min(surface) / 2)
        print(
            f"{package} {match[0]} {total}")
        grand_total += total

print(grand_total)
