# Advent of Code 2021 - Day 9 Part 2
# 9 Dec 2021 Brian Green
#
# Problem:
# What do you get if you multiply together the sizes of the three largest basins?
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
        low_points.append((y, x))

print(low_points)

checked_blocks = []


def find_basin(y, x):
    global checked_blocks
    checked_blocks.append((y, x))
    blocks = 1
    if (y, x - 1) not in checked_blocks and x != 0 and data_set[y][x - 1] != "9":
        blocks += find_basin(y, x - 1)
    if (
        (y, x + 1) not in checked_blocks
        and x != x_max - 1
        and data_set[y][x + 1] != "9"
    ):
        blocks += find_basin(y, x + 1)
    if (y - 1, x) not in checked_blocks and y != 0 and data_set[y - 1][x] != "9":
        blocks += find_basin(y - 1, x)
    if (
        (y + 1, x) not in checked_blocks
        and y != y_max - 1
        and data_set[y + 1][x] != "9"
    ):
        blocks += find_basin(y + 1, x)
    return blocks


basins = []
for y, x in low_points:
    basins.append(find_basin(y, x))

sorted_basins = sorted(basins)
print(sorted_basins)
print(sorted_basins[-1] * sorted_basins[-2] * sorted_basins[-3])
