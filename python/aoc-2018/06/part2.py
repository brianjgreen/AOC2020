# Advent of Code 2018 - Day 6 Part 2
# 25 Oct 2023 Brian Green
#
# Problem:
# What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?
#

from collections import Counter

import numpy as np
from part1 import get_coordinates, get_data, get_grid


def get_manhattan(grid, coord):
    # Add all of the manhattan distances to all coordinates, if less than 10000, this is a point in the region we want
    for key in grid.keys():
        total_dist = 0
        for point in coord:
            total_dist += np.abs(np.array(key) - np.array(point)).sum()
        if total_dist < 10000:
            grid[key] = 1

    return grid


def get_smallest_area(grid):
    # find the smallest area that contains points closest to all of the coordinates
    return Counter(grid.values()).most_common()[-1]


if __name__ == "__main__":
    coord, max_x, min_x, max_y, min_y = get_coordinates(get_data())
    grid = get_grid(max_x, min_x, max_y, min_y)
    manhattan = get_manhattan(grid, coord)
    value, count = get_smallest_area(manhattan)
    print(f"value={value} count={count}")
