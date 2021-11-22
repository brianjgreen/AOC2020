
# Advent of Code 2015 - Day 5 Part 2
# 17 Nov 2021 Brian Green
#
# Problem:
# How many strings are nice under these new rules?
#

import os

filename = "data" + os.sep + "brian_aoc201505.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

nice = 0

for message in data_set:
    # a pair of any two letters that appears at least twice in the string without overlapping
    pair = message[:2]
    remain = message[2:].strip()
    count = 0
    while len(remain) > 1:
        if pair in remain:
            count += 1
        pair = pair[1] + remain[0]
        remain = remain[1:]

    if count == 0:
        continue

    # at least one letter which repeats with exactly one letter between them
    double_gap = [i+j for i, j in zip(message, message[2:]) if i == j]
    if len(double_gap) == 0:
        continue

    nice += 1

print(nice)
