
# Advent of Code 2015 - Day 8 Part 2
# 21 Nov 2021 Brian Green
#
# Problem:
#

import os

filename = "data" + os.sep + "brian_aoc201508.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

total = 0
enc_total = 0
memory = 0

for item in data_set:
    mess = item.strip()[1: -1]
    total += len(mess) + 2
    enc_total += len(mess) + 6
    chars = list(mess)
    while len(chars) > 0:
        c = chars.pop(0)
        if c == '\\':
            enc_total += 1
            d = chars.pop(0)
            if d == '\\' or d == '\"':
                enc_total += 1
            elif d == 'x':
                chars.pop(0)
                chars.pop(0)
        memory += 1

print(total)
print(memory)
print(enc_total)
print(enc_total - total)
