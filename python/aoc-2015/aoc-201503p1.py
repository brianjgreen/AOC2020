# Advent of Code 2015 - Day 3 Part 1
# 17 Nov 2021 Brian Green
#
# Problem:
# how many houses receive at least one present?
#

import os

filename = "data" + os.sep + "brian_aoc201503.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

print(data_set[0])

houses = {(0, 0): 1}
x = 0
y = 0

for direction in data_set[0]:
    if direction == "^":
        print("north")
        y += 1
    elif direction == ">":
        print("east")
        x += 1
    elif direction == "<":
        print("west")
        x -= 1
    else:
        print("south")
        y -= 1

    if (x, y) in houses:
        houses[(x, y)] += 1
    else:
        houses[(x, y)] = 1

print(houses)
print(len(houses))
