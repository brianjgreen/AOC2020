
# Advent of Code 2022 - Day 3 Part 2
# 5 Dec 2022 Brian Green
#
# Problem:
# Rucksack Reorganization

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

# print(data_set)

# a = 97
# A = 65
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

total = 0

while len(data_set):
    first = data_set.pop()
    second = data_set.pop()
    third = data_set.pop()
    print(f'{first} {second} {third}')
    common = ''.join(set.intersection(*map(set,[first, second, third])))
    print(common)

    if ord(common) >= ord('a'):
        total += ord(common) - 96
    else:
        total += ord(common) - 38

print(total)
