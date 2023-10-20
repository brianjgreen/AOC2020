
# Advent of Code 2022 - Day 3 Part 2
# 19 Oct 2023 Brian Green
#
# Problem:
# What is the ID of the only claim that doesn't overlap?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

fabric = {}
claim = {}
for patch in data_set:
    cloth = patch.split()
    x_start, y_start = cloth[2][:-1].split(',')
    x_start = int(x_start)
    y_start = int(y_start)
    x_len, y_len = cloth[3].split('x')
    x_len = int(x_len)
    y_len = int(y_len)
    claim[cloth[0]] = []
    for x_offset in range(x_len):
        for y_offset in range(y_len):
            square = (x_start + x_offset, y_start + y_offset)
            claim[cloth[0]].append(square)
            if square in fabric:
                fabric[square] += 1
            else:
                fabric[square] = 1

for patch, coord in claim.items():
    clean = True
    for square in coord:
        if fabric[square] > 1:
            clean = False
    if clean:
        print(patch)
