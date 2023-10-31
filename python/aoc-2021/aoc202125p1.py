# Advent of Code 2021 - Day 24 Part 1
# 14 Nov 2022 Brian Green
#
# Problem:
# Track the movement of sea cucumbers
#

import os

filename = "data" + os.sep + "brian_aoc202125.dat"
with open(filename) as data_file:
    data_set = [pos.strip() for pos in data_file.readlines()]

test_data_1 = """
...>...
.......
......>
v.....>
......>
.......
..vvv..
"""

# print(test_data_1)
# data = test_data_1.splitlines()[1:]

test_data_2 = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""

# print(test_data_2)
# data = test_data_2.splitlines()[1:]

data = data_set
print(data)

sea = []
for row in data:
    sea.append(list(row))

for row in sea:
    print("".join(row))

next_col = 0
next_row = 0
max_col = len(sea[0])
max_row = len(sea)

steps = 0
changes = 1

while changes != 0:
    changes = 0
    steps += 1
    print()
    new_sea = [x[:] for x in sea]

    for row in range(max_row):
        for col in range(max_col):
            new_sea[row][col] = "."

    for row in range(max_row):
        for col in range(max_col):
            if new_sea[row][col] != ".":
                continue

            space = sea[row][col]
            if col + 1 >= max_col:
                next_col = 0
            else:
                next_col = col + 1

            if space == ">" and sea[row][next_col] == ".":
                new_sea[row][col] = "."
                new_sea[row][next_col] = ">"
                changes += 1
            else:
                new_sea[row][col] = space

    sea = new_sea
    new_sea = [x[:] for x in sea]

    for row in range(max_row):
        for col in range(max_col):
            new_sea[row][col] = "."

    for row in range(max_row):
        for col in range(max_col):
            if new_sea[row][col] != ".":
                continue

            space = sea[row][col]
            if row + 1 >= max_row:
                next_row = 0
            else:
                next_row = row + 1

            if space == "v" and sea[next_row][col] == ".":
                new_sea[row][col] = "."
                new_sea[next_row][col] = "v"
                changes += 1
            else:
                new_sea[row][col] = space

    sea = new_sea
    for row in sea:
        print("".join(row))
    print(f"changes={changes}, steps={steps}")
