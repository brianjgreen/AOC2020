# Advent of Code 2018 - Day 6 Part 1
# 25 Oct 2023 Brian Green
#
# Problem:
# What is the size of the largest area that isn't infinite?
#

from collections import Counter

import numpy as np

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

coord = []
max_x = 0
min_x = 1000
max_y = 0
min_y = 1000
for location in data_set:
    x, y = location.split(", ")
    x = int(x)
    y = int(y)
    # Find the boundaries of the field
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
    # Generate a list of coordinates
    coord.append((x, y))

grid = {}
# Generate the smallest field that contains all of the coordinates
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        grid[(x, y)] = 0

for key in grid.keys():
    man_dist = 1000
    for point in coord:
        # For each point in the field, find the nearest coordinate (there can be only one)
        curr_dist = np.abs(np.array(key) - np.array(point)).sum()
        if curr_dist == man_dist:
            # If a point is equidistant to multiple coordinates, then remove point from consideration
            grid[key] = None
            continue
        elif curr_dist < man_dist:
            grid[key] = point
            man_dist = curr_dist

# find the largest area that contains points closest to one of the coordinates
value, count = Counter(grid.values()).most_common(1)[0]
print(value)
print(count)
