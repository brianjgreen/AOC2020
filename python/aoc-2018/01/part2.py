
# Advent of Code 2018 - Day 1 Part 2
# 19 Oct 2023 Brian Green
#
# Problem:
# Which frequency does it reach twice?
#

import sys

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

freq = 0
all_freqs = []
while True:
    for adjust in data_set:
        num = adjust[1:]
        if adjust[0] == '-':
            freq -= int(num)
        else:
            freq += int(num)
        if freq in all_freqs:
            print(freq)
            sys.exit()
        else:
            all_freqs.append(freq)
