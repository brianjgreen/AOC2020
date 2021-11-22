
# Advent of Code 2015 - Day 8 Part 1
# 21 Nov 2021 Brian Green
#
# Problem:
# what is the number of characters of code for string literals minus the number of characters in memory
# for the values of the strings in total for the entire file?
#

import os

filename = "data" + os.sep + "brian_aoc201508.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

total = 0
memory = 0

for item in data_set:
    mess = item.strip()[1: -1]
    total += len(mess) + 2
    chars = list(mess)
    while len(chars) > 0:
        c = chars.pop(0)
        if c == '\\':
            d = chars.pop(0)
            if d == '\\' or d == '\"':
                pass
            elif d == 'x':
                chars.pop(0)
                chars.pop(0)
        memory += 1

print(total)
print(memory)
print(total - memory)
