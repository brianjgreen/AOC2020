
# Advent of Code 2021 - Day 8 Part 1
# 8 Dec 2021 Brian Green
#
# Problem:
# How much fuel must they spend to align to that position?
#

import os

filename = "data" + os.sep + "brian_aoc202108.dat"
with open(filename) as data_file:
    data_set = [pos.split() for pos in data_file.readlines()]

print(data_set)

count = 0
unique_segments = [2, 3, 4, 7]
for message in data_set:
    for data in message[11:]:
        if len(data) in unique_segments:
            count += 1

print(count)
