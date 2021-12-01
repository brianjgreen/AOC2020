
# Advent of Code 2021 - Day 1 Part 1
# 1 Dec 2021 Brian Green
#
# Problem:
# How many measurements are larger than the previous measurement?
#

import os

filename = "data" + os.sep + "brian_aoc202101.dat"
with open(filename) as data_file:
    data_set = [int(num) for num in data_file.readlines()]

total_increases = 0
for pos in range(len(data_set) - 1):
    if data_set[pos + 1] > data_set[pos]:
        total_increases += 1

print(total_increases)
