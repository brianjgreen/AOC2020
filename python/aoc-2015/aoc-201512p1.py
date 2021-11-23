
# Advent of Code 2015 - Day 12 Part 1
# 22 Nov 2021 Brian Green
#
# Problem:
# What is the sum of all numbers in the document?
#

import os
import re

filename = "data" + os.sep + "brian_aoc201512.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set[0])

pattern = re.compile(r"-{0,1}\d+")
matches = re.findall(pattern, data_set[0])
# print(matches)

total = 0
for i in matches:
    total += int(i)

print(total)
