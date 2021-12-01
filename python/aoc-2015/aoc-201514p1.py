
# Advent of Code 2015 - Day 14 Part 1
# 30 Nov 2021 Brian Green
#
# Problem:
# What distance has the winning reindeer traveled?
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
    roster[name] = list([speed for i in range(duration)] +
                        [0 for i in range(cooldown)])

# print(roster)

log = {deer: 0 for deer in roster}

for t in range(2503):
    for deer in roster:
        log[deer] += roster[deer][t % len(roster[deer])]


print(log)
print(max(log.values()))
