
# Advent of Code 2018 - Day 6 Part 2
# 25 Oct 2023 Brian Green
#
# Problem:
# What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?
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
    x, y = location.split(', ')
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

# Add all of the manhattan distances to all coordinates, if less than 10000, this is a point in the region we want
for key in grid.keys():
    total_dist = 0
    for point in coord:
        total_dist += np.abs(np.array(key) - np.array(point)).sum()
    if total_dist < 10000:
        grid[key] = 1

# find the smallest area that contains points closest to all of the coordinates
value, count = Counter(grid.values()).most_common()[-1]
print(value)
print(count)
