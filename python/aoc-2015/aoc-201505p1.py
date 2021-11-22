
# Advent of Code 2015 - Day 5 Part 1
# 17 Nov 2021 Brian Green
#
# Problem:
# How many strings are nice?
#

import os

filename = "data" + os.sep + "brian_aoc201505.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

nice = 0

for message in data_set:
    # at least three vowels
    vowels = 0
    for letter in 'aeiou':
        vowels += message.count(letter)
    if vowels < 3:
        continue

    # at least one letter appears twice in a row
    doubles = [i+j for i, j in zip(message, message[1:]) if i == j]
    if len(doubles) == 0:
        continue

    # does not contain the strings ab, cd, pq, or xy
    if 'ab' in message or 'cd' in message or 'pq' in message or 'xy' in message:
        continue

    nice += 1

print(nice)
