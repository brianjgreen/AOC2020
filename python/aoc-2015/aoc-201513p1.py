# Advent of Code 2015 - Day 13 Part 1
# 29 Nov 2021 Brian Green
#
# Problem:
# What is the total change in happiness for the optimal seating arrangement of the actual guest list?
#

import itertools
import os

filename = "data" + os.sep + "brian_aoc201513.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)
happiness = {}

for happy in data_set:
    level = happy.split()
    person = level[0]
    change = level[2]
    gain_loss = 1
    if change == "lose":
        gain_loss = -1
    units = int(level[3]) * gain_loss
    neighbor = level[-1][:-1]
    # print(f"{person} {units} {neighbor}")
    if person in happiness:
        happiness[person][neighbor] = units
    else:
        happiness[person] = {neighbor: units}

# print(json.dumps(happiness, indent=4))

people = list(happiness.keys())
# print(people)

total_people = len(people)

most_happy = 0


def get_happy(people):
    left = -1
    right = 1
    happy_people = {p: 0 for p in people}

    for p in people:
        # print(f"{people[left]} <- {p} -> {people[right]}")
        happy_people[p] += happiness[p][people[left]] + happiness[p][people[right]]
        left += 1
        right += 1
        if right >= total_people:
            right = 0

    # print(happy_people)
    return sum(happy_people.values())


all_combos = list(itertools.permutations(people))
# print(len(all_combos))
for combo in all_combos:
    total_happiness = get_happy(list(combo))
    if total_happiness > most_happy:
        most_happy = total_happiness

print(most_happy)
