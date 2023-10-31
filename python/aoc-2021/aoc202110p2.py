# Advent of Code 2021 - Day 10 Part 2
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
# print(data_set)


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


points = {"(": 1, "[": 2, "{": 3, "<": 4}
grand_total = []
incomplete = []
# tabulate = {'[': 0, '(': 0, '{': 0, '<': 0}
for data in data_set:
    # print(data)
    new_data = reduce_chunks(data)
    # print(new_data)
    if (
        ">" not in new_data
        and "}" not in new_data
        and ")" not in new_data
        and "]" not in new_data
    ):
        incomplete.append(new_data)

print(incomplete)

for data in incomplete:
    total = 0
    for d in data[::-1]:
        total *= 5
        total += points[d]
    grand_total.append(total)

print(grand_total)
grand_total = sorted(grand_total)
print(grand_total[(len(grand_total) - 1) // 2])
