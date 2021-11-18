
# Advent of Code 2015 - Day 3 Part 2
# 17 Nov 2021 Brian Green
#
# Problem:
#

import os

filename = "data" + os.sep + "brian_aoc201503.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

print(data_set[0])

houses = {(0, 0): 1}
dalek = {}
x = 0
y = 0
dalek_x = 0
dalek_y = 0

santa = True

for direction in data_set[0]:
    if direction == '^':
        if santa:
            y += 1
        else:
            dalek_y += 1
    elif direction == '>':
        if santa:
            x += 1
        else:
            dalek_x += 1
    elif direction == '<':
        if santa:
            x -= 1
        else:
            dalek_x -= 1
    else:
        if santa:
            y -= 1
        else:
            dalek_y -= 1

    if santa:
        santa = False
        if (x, y) in houses:
            houses[(x, y)] += 1
        else:
            if (x, y) not in dalek:
                houses[(x, y)] = 1
    else:
        santa = True
        if (dalek_x, dalek_y) in dalek:
            dalek[(dalek_x, dalek_y)] += 1
        else:
            if (dalek_x, dalek_y) not in houses:
                dalek[(dalek_x, dalek_y)] = 1

print(houses)
print(dalek)
print(len(houses))
print(len(dalek))
total = len(houses) + len(dalek)
print(total)
