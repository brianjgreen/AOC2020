#
# Advent of Code 2016 - Day 1 Part 1
# 1 Dec 2021 Brian Green
#
# Problem:
# How many blocks away is Easter Bunny HQ?
#

import os

filename = "data" + os.sep + "brian_aoc201602.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

testcase1 = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

max_x = 2
max_y = 2


def get_code(instructions):
    x = 1
    y = 1
    code = []
    for step in instructions:
        for move in step.strip():
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'R':
                x += 1
            elif move == 'L':
                x -= 1
            else:
                print(f"{move} WHAT?!?")

            if x < 0:
                x = 0
            elif x > max_x:
                x = max_x

            if y < 0:
                y = 0
            elif y > max_y:
                y = max_y
        code.append(keypad[y][x])

    return code


print(get_code(testcase1))
print(get_code(data_set))
