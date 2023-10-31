# Advent of Code 2021 - Day 1 Part 2
# 1 Dec 2021 Brian Green
#
# Problem:
# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
#

import os

filename = "data" + os.sep + "brian_aoc202101.dat"
with open(filename) as data_file:
    data_set = [int(num) for num in data_file.readlines()]

total_increases = 0
for pos in range(len(data_set) - 3):
    if (
        data_set[pos + 1] + data_set[pos + 2] + data_set[pos + 3]
        > data_set[pos] + data_set[pos + 1] + data_set[pos + 2]
    ):
        total_increases += 1

print(total_increases)
