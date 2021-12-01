
# Advent of Code 2015 - Day 15 Part 1
# 1 Dec 2021 Brian Green
#
# Problem:
# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?
#

import json
import os

filename = "data" + os.sep + "brian_aoc201515.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

print(data_set)

stats = {}

for ingredient in data_set:
    pantry = ingredient.split()
    print(pantry)
    name = pantry[0][:-1]
    cap = int(pantry[2][:-1])
    dur = int(pantry[4][:-1])
    fla = int(pantry[6][:-1])
    tex = int(pantry[8][:-1])
    cal = int(pantry[10])

    stats[name] = {'capacity': cap, 'durability': dur,
                   'flavor': fla, 'texture': tex, 'calories': cal}

print(json.dumps(stats, indent=4))

highest_total = 0
for sugar in range(100):
    for sprinkles in range(100):
        for candy in range(100):
            for chocolate in range(100):
                if sugar + sprinkles + candy + chocolate != 100:
                    continue

                cal = sugar * stats['Sugar']['calories'] + \
                    sprinkles * stats['Sprinkles']['calories'] + \
                    candy * stats['Candy']['calories'] + \
                    chocolate * stats['Chocolate']['calories']
                if cal != 500:
                    continue

                cap = sugar * stats['Sugar']['capacity'] + \
                    sprinkles * stats['Sprinkles']['capacity'] + \
                    candy * stats['Candy']['capacity'] + \
                    chocolate * stats['Chocolate']['capacity']
                if cap < 0:
                    cap = 0

                dur = sugar * stats['Sugar']['durability'] + \
                    sprinkles * stats['Sprinkles']['durability'] + \
                    candy * stats['Candy']['durability'] + \
                    chocolate * stats['Chocolate']['durability']
                if dur < 0:
                    dur = 0

                fla = sugar * stats['Sugar']['flavor'] + \
                    sprinkles * stats['Sprinkles']['flavor'] + \
                    candy * stats['Candy']['flavor'] + \
                    chocolate * stats['Chocolate']['flavor']
                if fla < 0:
                    fla = 0

                tex = sugar * stats['Sugar']['texture'] + \
                    sprinkles * stats['Sprinkles']['texture'] + \
                    candy * stats['Candy']['texture'] + \
                    chocolate * stats['Chocolate']['texture']
                if tex < 0:
                    text = 0

                total = cap * dur * fla * tex
                if total > highest_total:
                    highest_total = total

print(highest_total)
