#
# Advent of Code 2016 - Day 3 Part 2
# 10 May 2022 Brian Green
#
# Problem:
#

import os

filename = "data" + os.sep + "brian_aoc201603.dat"
with open(filename) as data_file:
    data_set = [list(map(int, nums.split())) for nums in data_file.readlines()]

# print(data_set)
num_tri = 0
pos = 0
block = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for a, b, c in data_set:
    index = pos % 3
    block[0][index] = a
    block[1][index] = b
    block[2][index] = c

    if index == 2:
        print(block)
        for x, y, z in block:
            if x + y > z and y + z > x and x + z > y:
                num_tri += 1
    pos += 1

print(num_tri)
