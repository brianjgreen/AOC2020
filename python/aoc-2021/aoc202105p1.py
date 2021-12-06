
# Advent of Code 2021 - Day 5 Part 1
# 5 Dec 2021 Brian Green
#
# Problem:
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
#

import os

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

print(data_set)

sub_map = {}

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
        start = min(y1, y2)
        end = max(y1, y2)
        for y in range(start, end + 1):
            key = (x1, y)
            if key in sub_map:
                sub_map[key] += 1
            else:
                sub_map[key] = 1
    elif y1 == y2:
        start = min(x1, x2)
        end = max(x1, x2)
        for x in range(start, end + 1):
            key = (x, y1)
            if key in sub_map:
                sub_map[key] += 1
            else:
                sub_map[key] = 1

print(sub_map)
count = 0
for val in sub_map.values():
    if val > 1:
        count += 1

print(count)
