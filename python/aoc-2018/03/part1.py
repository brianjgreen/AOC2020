
# Advent of Code 2022 - Day 3 Part 1
# 19 Oct 2023 Brian Green
#
# Problem:
# How many square inches of fabric are within two or more claims?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

fabric = {}
for patch in data_set:
    cloth = patch.split()
    x_start, y_start = cloth[2][:-1].split(',')
    x_start = int(x_start)
    y_start = int(y_start)
    x_len, y_len = cloth[3].split('x')
    x_len = int(x_len)
    y_len = int(y_len)
    for x_offset in range(x_len):
        for y_offset in range(y_len):
            square = (x_start + x_offset, y_start + y_offset)
            if square in fabric:
                fabric[square] += 1
            else:
                fabric[square] = 1

overlap = 0
for square in fabric:
    if fabric[square] > 1:
        overlap += 1

print(overlap)
