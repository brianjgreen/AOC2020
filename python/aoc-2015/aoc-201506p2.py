
# Advent of Code 2015 - Day 6 Part 2
# 18 Nov 2021 Brian Green
#
# Problem:
# What is the total brightness of all lights combined after following Santa's instructions?
#

import os
import re

lights = {}


def turn_on(start_x, start_y, end_x, end_y, dir):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            if (x, y) in lights:
                if dir < 0 and lights[(x, y)] < 1:
                    pass
                else:
                    lights[(x, y)] += dir
            else:
                if dir > 0:
                    lights[(x, y)] = dir


filename = "data" + os.sep + "brian_aoc201506.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

pattern = re.compile("(\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})")
for instruction in data_set:
    coordinates = re.findall(pattern, instruction)[0]
    start_x, start_y, end_x, end_y = coordinates

    if 'turn on' in instruction:
        turn_on(start_x, start_y, end_x, end_y, 1)
    elif 'turn off' in instruction:
        turn_on(start_x, start_y, end_x, end_y, -1)
    else:
        turn_on(start_x, start_y, end_x, end_y, 2)

lights_on = 0
for bulb in lights:
    lights_on += lights[bulb]

print(lights_on)
