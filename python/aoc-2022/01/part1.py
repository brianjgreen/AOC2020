# Advent of Code 2022 - Day 1 Part 1
# 1 Dec 2022 Brian Green
#
# Problem:
# Which Elf has the most calories?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

print(data_set)

elf = 1
top_elf = 1
most_calories = 0
calories = 0

for food in data_set:
    if food == "":
        if calories > most_calories:
            most_calories = calories
            top_elf = elf
        calories = 0
        elf += 1
    else:
        calories += int(food)

print(f"elf={top_elf} cal={most_calories}")
