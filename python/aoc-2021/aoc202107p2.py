
# Advent of Code 2021 - Day 7 Part 2
# 7 Dec 2021 Brian Green
#
# Problem:
# How much fuel must they spend to align to that position?
#

import os
from typing import MutableMapping

filename = "data" + os.sep + "brian_aoc202107.dat"
with open(filename) as data_file:
    data_set = [pos.split(',') for pos in data_file.readlines()][0]

testcase = """16,1,2,0,4,2,7,1,2,14"""

# data_set = testcase.split(',')

crabs = [int(pos) for pos in data_set]

print(crabs)

min_fuel = 1000000000
for i in range(min(crabs), max(crabs) + 1):
    total_fuel = 0
    for pos in crabs:
        total_fuel += sum(range(abs(pos - i) + 1))
        if total_fuel >= min_fuel:
            break

    if total_fuel < min_fuel:
        min_fuel = total_fuel

print(min_fuel)
