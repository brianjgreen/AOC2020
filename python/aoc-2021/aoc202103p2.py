
# Advent of Code 2021 - Day 3 Part 2
# 3 Dec 2021 Brian Green
#
# Problem:
# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating,
# then multiply them together. What is the life support rating of the submarine?
# (Be sure to represent your answer in decimal, not binary.)
#

import os

filename = "data" + os.sep + "brian_aoc202103.dat"
with open(filename) as data_file:
    data_set = [binary.strip() for binary in data_file.readlines()]

testcase = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

# data_set = testcase.split()
size = len(data_set[0])


def popular_bits(data_set, mask):
    ones_set = []
    nils_set = []
    for diag in data_set:
        if mask & int(diag, 2) != 0:
            ones_set.append(diag)
        else:
            nils_set.append(diag)

    if len(ones_set) >= len(nils_set):
        return ones_set.copy()
    else:
        return nils_set.copy()


def unpopular_bits(data_set, mask):
    ones_set = []
    nils_set = []
    for diag in data_set:
        if mask & int(diag, 2) != 0:
            ones_set.append(diag)
        else:
            nils_set.append(diag)

    if len(ones_set) < len(nils_set):
        return ones_set.copy()
    else:
        return nils_set.copy()


popular_data = data_set.copy()
mask = 1 << (size - 1)
while len(popular_data) != 1:
    popular_data = popular_bits(popular_data, mask)
    # print(popular_data)
    mask >>= 1
oxy = int(popular_data[0], 2)

mask = 1 << (size - 1)
while len(data_set) != 1:
    data_set = unpopular_bits(data_set, mask)
    # print(data_set)
    mask >>= 1
car = int(data_set[0], 2)

print(f"{oxy * car}")
