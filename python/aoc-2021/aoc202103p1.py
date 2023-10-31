# Advent of Code 2021 - Day 3 Part 1
# 3 Dec 2021 Brian Green
#
# Problem:
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
# What is the power consumption of the submarine?
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

elements = len(data_set)
size = len(data_set[0])
counter = [0 for x in range(size)]

for diag in data_set:
    num = int(diag, 2)
    for bit in range(size):
        mask = 1 << bit
        if num & mask != 0:
            counter[bit] += 1

print(counter)
gamma = 0
epsilon = 0

for bit in range(size):
    mask = 1 << bit
    if counter[bit] > (elements / 2):
        gamma |= mask
    else:
        epsilon |= mask

print(gamma)
print(epsilon)
print(f"{gamma * epsilon}")
