# python day18.py ../../data/2015/day18.dat

import sys
import numpy as np


def parse_input(input_data):
    data_set = input_data.strip().split("\n")
    rows = len(data_set)
    cols = len(data_set[0])
    field = np.zeros((rows, cols), dtype=np.int8)
    for x in range(cols):
        for y in range(rows):
            if data_set[x][y] == "#":
                field[x, y] = 1
    return field


def part1(field):
    num_steps = 100
    rows, cols = field.shape
    for _ in range(num_steps):
        new_field = np.zeros((rows, cols), dtype=np.int8)
        for x in range(cols):
            for y in range(rows):
                start_x = x - 1 if x > 0 else x
                start_y = y - 1 if y > 0 else y
                end_x = x + 1 if x < cols - 1 else cols
                end_y = y + 1 if y < rows - 1 else rows
                subfield = field[start_x:end_x + 1, start_y:end_y + 1]
                if field[x, y] == 1 and (subfield.sum() == 3 or subfield.sum() == 4):
                    new_field[x, y] = 1
                if field[x, y] == 0 and subfield.sum() == 3:
                    new_field[x, y] = 1
        field = new_field.copy()
    return field.sum()


def part2(field):
    num_steps = 100
    rows, cols = field.shape
    field[0, 0] = 1
    field[0, cols - 1] = 1
    field[rows - 1, 0] = 1
    field[rows - 1, cols - 1] = 1
    for _ in range(num_steps):
        new_field = np.zeros((rows, cols), dtype=np.int8)
        for x in range(cols):
            for y in range(rows):
                start_x = x - 1 if x > 0 else x
                start_y = y - 1 if y > 0 else y
                end_x = x + 1 if x < cols - 1 else cols
                end_y = y + 1 if y < rows - 1 else rows
                subfield = field[start_x:end_x + 1, start_y:end_y + 1]
                if field[x, y] == 1 and (subfield.sum() == 3 or subfield.sum() == 4):
                    new_field[x, y] = 1
                if field[x, y] == 0 and subfield.sum() == 3:
                    new_field[x, y] = 1
        field = new_field.copy()
        field[0, 0] = 1
        field[0, cols - 1] = 1
        field[rows - 1, 0] = 1
        field[rows - 1, cols - 1] = 1
    return field.sum()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_data = f.read()
    else:
        input_data = """.#.#.#
...#..
#....#
..#...
#.#..#
####.#
..#.#.
"""
    field = parse_input(input_data)
    print("Day 18 Part 1:", part1(field))
    print("Day 18 Part 2:", part2(field))
