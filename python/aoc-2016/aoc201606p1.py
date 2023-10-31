# Advent of Code 2016 - Day 6 Parts 1 and 2
# 20 May 2023 Brian Green
#
# Problem:
# Day 6: Signals and Noise
# What is the error-corrected version of the message being sent?
#

from collections import Counter

# filename = "test06.dat"
filename = "data06.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

for col in range(len(data_set[0])):
    column = Counter([row[col] for row in data_set])
    # print(column.most_common(1)[0][0], end="")    # Part 1
    print(column.most_common()[-1][0], end="")  # Part 2

print()
