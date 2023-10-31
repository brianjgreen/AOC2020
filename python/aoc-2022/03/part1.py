# Advent of Code 2022 - Day 3 Part 1
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

for sack in data_set:
    first_comp = sack[: len(sack) // 2]
    second_comp = sack[len(sack) // 2 :]
    item = "".join(set(first_comp).intersection(second_comp))
    print(item)
    if ord(item) >= ord("a"):
        total += ord(item) - 96
        print(f"lower {item} {ord(item)} {ord(item) - 96}")
    else:
        total += ord(item) - 38
        print(f"upper {item} {ord(item)} {ord(item) - 38}")
print(total)
