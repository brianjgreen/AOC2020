# Advent of Code 2015 - Day 14 Part 2
# 30 Nov 2021 Brian Green
#
# Problem:
# How many points does the winning reindeer have?
#

import os

filename = "data" + os.sep + "brian_aoc201514.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

# print(data_set)

roster = {}

for deer in data_set:
    stats = deer.split()
    name = stats[0]
    speed = int(stats[3])
    duration = int(stats[6])
    cooldown = int(stats[13])
    # print(f"{name} {speed} {duration} {cooldown}")
    roster[name] = list([speed for i in range(duration)] + [0 for i in range(cooldown)])

# print(roster)

log = {deer: 0 for deer in roster}
points = {deer: 0 for deer in roster}

for t in range(2503):
    for deer in roster:
        log[deer] += roster[deer][t % len(roster[deer])]

    winner = max(log.values())
    awards = [k for k, v in log.items() if v == winner]
    for deer in awards:
        points[deer] += 1

print(points)
print(max(points.values()))
