
# Advent of Code 2021 - Day 10 Part 1
# 10 Dec 2021 Brian Green
#
# Problem:
# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
#

import os

filename = "data" + os.sep + "brian_aoc202110.dat"
with open(filename) as data_file:
    data_set = [pos.strip() for pos in data_file.readlines()]

testdata = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

# data_set = testdata.split()
print(data_set)


def reduce_chunks(data):
    prev_data = ""
    next_data = data
    while prev_data != next_data:
        prev_data = next_data
        next_data = next_data.replace("()", "")
        next_data = next_data.replace("[]", "")
        next_data = next_data.replace("<>", "")
        next_data = next_data.replace("{}", "")

    return next_data


points = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0
# tabulate = {'[': 0, '(': 0, '{': 0, '<': 0}
for data in data_set:
    print(data)
    new_data = reduce_chunks(data)
    print(new_data)

    for c in new_data:
        if c in ">})]":
            print(c)
            print(points[c])
            total += points[c]
            break
    print()
print(total)
