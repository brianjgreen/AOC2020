# Advent of Code 2018 - Day 6 Part 1
# 25 Oct 2023 Brian Green
#
# Problem:
# What is the size of the largest area that isn't infinite?
#

from collections import Counter

import numpy as np


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_coordinates(data_set):
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

    return coord, max_x, min_x, max_y, min_y


def get_grid(max_x, min_x, max_y, min_y):
    grid = {}
    # Generate the smallest field that contains all of the coordinates
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            grid[(x, y)] = 0

    return grid


def populate_grid(grid, coord):
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

    return grid


def get_largest_area(grid):
    # find the largest area that contains points closest to one of the coordinates
    return Counter(grid.values()).most_common(1)[0]


if __name__ == "__main__":
    coord, max_x, min_x, max_y, min_y = get_coordinates(get_data())
    grid = get_grid(max_x, min_x, max_y, min_y)
    pop_grid = populate_grid(grid, coord)
    value, count = get_largest_area(pop_grid)
    print(f"value={value} count={count}")
