# Advent of Code 2017 - Day 2 Part 2
# 29 Nov 2023 Brian Green
#
# Problem:
# What is the sum of each row's result?
#

from itertools import permutations

from part1 import get_data, split_data


def calc_checksum(data):
    checksum = 0
    for row in data:
        for combo in permutations(row, 2):
            if combo[0] % combo[1] == 0:
                checksum += int(combo[0] / combo[1])
                continue
    return checksum


if __name__ == "__main__":
    data = split_data(get_data())
    print(calc_checksum(data))
