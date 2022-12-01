
# Advent of Code 2022 - Day 1 Part 2
# 1 Dec 2022 Brian Green
#
# Problem:
# Which top 3 Elves has the most calories?
#

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

print(data_set)

elf = 1
calories = []
acc_cal = 0

for food in data_set:
    if food == '':
        calories.append(acc_cal)
        elf += 1
        acc_cal = 0
    else:
        acc_cal += int(food)
calories.append(acc_cal)

calories = sorted(calories, reverse=True)
print(calories)
print(calories[0] + calories[1] + calories[2])
