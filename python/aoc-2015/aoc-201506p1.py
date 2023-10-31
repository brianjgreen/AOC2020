# Advent of Code 2015 - Day 6 Part 1
# 17 Nov 2021 Brian Green
#
# Problem:
# set up your lights by doing the instructions Santa sent you in order.
#

import os
import re

lights = {}


def turn_on(start_x, start_y, end_x, end_y, dir):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            lights[(x, y)] = dir


def toggle(start_x, start_y, end_x, end_y):
    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            if (x, y) in lights:
                if lights[(x, y)]:
                    lights[(x, y)] = False
                else:
                    lights[(x, y)] = True
            else:
                lights[(x, y)] = True


filename = "data" + os.sep + "brian_aoc201506.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

pattern = re.compile(r"(\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})")
for instruction in data_set:
    coordinates = re.findall(pattern, instruction)[0]
    start_x, start_y, end_x, end_y = coordinates

    if "turn on" in instruction:
        turn_on(start_x, start_y, end_x, end_y, True)
    elif "turn off" in instruction:
        turn_on(start_x, start_y, end_x, end_y, False)
    else:
        toggle(start_x, start_y, end_x, end_y)

lights_on = 0
for bulb in lights:
    if lights[bulb]:
        lights_on += 1

print(lights_on)
