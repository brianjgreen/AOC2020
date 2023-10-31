# Advent of Code 2021 - Day 9 Part 1
# 9 Dec 2021 Brian Green
#
# Problem:
# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
#

import os

filename = "data" + os.sep + "brian_aoc202109.dat"
with open(filename) as data_file:
    data_set = [pos.strip() for pos in data_file.readlines()]

testdata = """2199943210
3987894921
9856789892
8767896789
9899965678"""

# data_set = testdata.split()
print(data_set)

y_max = len(data_set)
x_max = len(data_set[0])
print(x_max)
print(y_max)

low_points = []

for x in range(x_max):
    for y in range(y_max):
        test_point = data_set[y][x]
        if x != 0 and test_point >= data_set[y][x - 1]:
            continue
        if x != x_max - 1 and test_point >= data_set[y][x + 1]:
            continue
        if y != 0 and test_point >= data_set[y - 1][x]:
            continue
        if y != y_max - 1 and test_point >= data_set[y + 1][x]:
            continue
        low_points.append(int(test_point) + 1)

print(sum(low_points))
