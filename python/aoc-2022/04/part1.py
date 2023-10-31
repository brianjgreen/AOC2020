# Advent of Code 2022 - Day 4 Part 1
# 5 Dec 2022 Brian Green
#
# Problem:
# Camp cleanup, find overlapping chores

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

# print(data_set)

total = 0
for elf in data_set:
    pair = elf.split(",")
    # print(pair)
    elf_one = pair[0].split("-")
    elf_two = pair[1].split("-")
    # print(f"{elf_one} {elf_two}")
    elf_one = list(range(int(elf_one[0]), int(elf_one[1]) + 1))
    elf_two = list(range(int(elf_two[0]), int(elf_two[1]) + 1))
    # print(f"{elf_one} {elf_two}")
    # print(all(x in elf_one for x in elf_two) or all(x in elf_two for x in elf_one))
    if all(x in elf_one for x in elf_two) or all(x in elf_two for x in elf_one):
        total += 1

print(total)
