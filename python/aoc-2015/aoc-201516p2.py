# Advent of Code 2015 - Day 16 Part 1
# 7 Dec 2021 Brian Green
#
# Problem:
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
#

import os

filename = "data" + os.sep + "brian_aoc201516.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

matching_aunt = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

aunts = {}
for sue in data_set:
    attribs = sue.split()
    # print(attribs)
    aunts[attribs[1][:-1]] = {
        attribs[2][:-1]: int(attribs[3][:-1]),
        attribs[4][:-1]: int(attribs[5][:-1]),
        attribs[6][:-1]: int(attribs[7]),
    }

eligible_aunts = []
for sue in aunts:
    i = 0
    for k, v in aunts[sue].items():
        if k == "cats" or k == "trees":
            if v > matching_aunt[k]:
                i += 1
        elif k == "pomeranians" or k == "goldfish":
            if v < matching_aunt[k]:
                i += 1
        else:
            if v == matching_aunt[k]:
                i += 1
    if i == 3:
        eligible_aunts.append(sue)

print(eligible_aunts)
for sue in eligible_aunts:
    print(aunts[sue])
