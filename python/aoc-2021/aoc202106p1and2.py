# Advent of Code 2021 - Day 6 Part 1 and 2
# 6 Dec 2021 Brian Green
#
# Problem:
# Part 1: How many lanternfish would there be after 80 days?
# Part 2: How many lanternfish would there be after 256 days?
#

import os

filename = "data" + os.sep + "brian_aoc202106.dat"
with open(filename) as data_file:
    data_set = [fish.split(",") for fish in data_file.readlines()][0]

testcase = """3,4,3,1,2"""

# data_set = testcase.split(',')

school = [int(fish) for fish in data_set]
# print(school)

# total_days = 80  # PART 1
total_days = 256  # PART 2


def calc_school(my_school):
    for day in range(int(total_days / 2)):
        # print(f"day {day}")
        new_school = []
        for fish in my_school:
            if fish == 0:
                new_school.append(6)
                new_school.append(8)
            else:
                new_school.append(fish - 1)
        my_school = new_school
    return my_school


super_school = [0 for x in range(9)]
num_school = [0 for x in range(9)]
total_school = []
for i in range(9):
    new_school = calc_school(
        [
            i,
        ]
    )
    super_school[i] = new_school
    num_school[i] = len(new_school)

for i in school:
    total_school += super_school[i]

total = 0
for fish in total_school:
    total += num_school[fish]

print(f"total {total}")
