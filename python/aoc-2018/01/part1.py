# Advent of Code 2018 - Day 1 Part 1
# 19 Oct 2023 Brian Green
#
# Problem:
# What is the resulting frequency?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

freq = 0
for adjust in data_set:
    num = adjust[1:]
    # print(num)
    if adjust[0] == "-":
        freq -= int(num)
    else:
        freq += int(num)

print(freq)
