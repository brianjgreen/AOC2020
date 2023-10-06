#
# Advent of Code 2016 - Day 3 Part 1
# 2 May 2022 Brian Green
#
# Problem:
#

import os

filename = "data" + os.sep + "brian_aoc201603.dat"
with open(filename) as data_file:
    data_set = [list(map(int,nums.split())) for nums in data_file.readlines()]

print(data_set)
num_tri = 0
for a, b, c in data_set:
    if a+b > c and b + c > a and a + c > b:
        num_tri += 1

print(num_tri)
