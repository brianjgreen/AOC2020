# Advent of Code 2015 - Day 19 Part 1
# 17 May 2023 Brian Green
#
# Problem:
# Day 19: Medicine for Rudolph
# How many distinct molecules can be created?
#

import re

# filename = "test19.dat"
filename = "data19.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

print(data_set)

formula = data_set[-1]
subs = {}

# Create a dictionary of the molecule substitutions
for instruction in data_set:
    if "=>" in instruction:
        key, value = instruction.split(" => ")
        if key in subs:
            subs[key].append(value)
        else:
            subs[key] = [
                value,
            ]

print(subs)
print(formula)
new_formulas = []

# Substitute one molecule at a time
for key, values in subs.items():
    for match in re.finditer(key, formula):
        start, end = match.span()
        for val in values:
            new_formulas.append(formula[:start] + val + formula[end:])

print(new_formulas)
print(len(new_formulas))
print(len(set(new_formulas)))
