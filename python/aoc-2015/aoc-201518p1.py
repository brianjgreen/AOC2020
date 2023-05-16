
# Advent of Code 2015 - Day 18 Part 1
# 15 May 2023 Brian Green
#
# Problem:
# Day 18: Like a GIF For Your Yard
# How many lights are on after X steps?
#

import numpy as np
import time

# filename = "test18.dat"
# num_steps = 4
filename = "data18.dat"
num_steps = 100
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

# print(data_set)
rows = len(data_set)
cols = len(data_set[0])

# Create an array of zeros
field = np.zeros((rows, cols), dtype=np.int8)

# Convert the data from . and # chars into 0 and 1 integers
for x in range(cols):
    for y in range(rows):
        if data_set[x][y] == '#':
            field[x, y] = 1
# print(field)

for animation_frame in range(num_steps):
    new_field = np.zeros((rows, cols), dtype=np.int8)

    for x in range(cols):
        for y in range(rows):
            # Calculate a subset of surrounding lights around the current light
            # Lights on the perimeter only count adjacent lights in bounds of the array
            start_x = (x - 1 if x > 0 else x)
            start_y = (y - 1 if y > 0 else y)
            end_x = (x + 1 if x < cols - 1 else cols)
            end_y = (y + 1 if y < rows - 1 else rows)
            subfield = field[start_x:end_x + 1, start_y: end_y + 1]
            # print(subfield)

            # If light is on and 2 or 4 adjacent lights are on, stay on
            if field[x, y] == 1 and (subfield.sum() == 3 or subfield.sum() == 4):
                new_field[x, y] = 1

            # if light is off and 3 adjacent lights are on, turn on
            if field[x, y] == 0 and subfield.sum() == 3:
                new_field[x, y] = 1

    # print(new_field)
    field = new_field.copy()

print(new_field.sum())
