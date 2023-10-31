
# Advent of Code 2021 - Day 5 Part 2
# 5 Dec 2021 Brian Green
#
# Problem:
# Consider all of the lines. At how many points do at least two lines overlap?
#

import os
from collections import defaultdict

filename = "data" + os.sep + "brian_aoc202105.dat"
with open(filename) as data_file:
    data_set = [coord.strip() for coord in data_file.readlines()]

testcase = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

# data_set = testcase.split('\n')

# print(data_set)

sub_map = defaultdict(int)

for coord in data_set:
    x, y = coord.split(' -> ')
    # print(f"{x} {y}")
    x1, y1 = x.split(',')
    x2, y2 = y.split(',')
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            sub_map[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            sub_map[(x, y1)] += 1
    elif abs(x1-x2) == abs(y1-y2):
        # print(f"{x1},{y1} {x2},{y2}")
        if x1 < x2:
            x_step = 1
        else:
            x_step = -1
        if y1 < y2:
            y_step = 1
        else:
            y_step = -1
        y = y1
        for x in range(x1, x2 + x_step, x_step):
            sub_map[(x, y)] += 1
            y += y_step

# print(sub_map)
count = 0
for val in sub_map.values():
    if val > 1:
        count += 1

print(count)
