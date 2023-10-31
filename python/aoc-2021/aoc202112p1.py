
# Advent of Code 2021 - Day 12 Part 1
# 22 Dec 2021 Brian Green
#
# Problem:
# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
#

import os
from collections import defaultdict

filename = "data" + os.sep + "brian_aoc202112.dat"
with open(filename) as data_file:
    data_set = [pos.strip() for pos in data_file.readlines()]

testdata = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

testdata2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

testdata3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

# data_set = testdata.split()
# data_set = testdata2.split()
# data_set = testdata3.split()

print(data_set)

map_steps = defaultdict(list)

for step in data_set:
    key, value = step.split('-')
    if value == 'start' or value == 'end':
        temp_val = key
        key = value
        value = temp_val
    map_steps[key].append(value)

print(map_steps)
temp_map_steps = map_steps.copy()
for key, values in temp_map_steps.items():
    if key == 'start':
        continue
    for v in values:
        if v == 'start' or v == 'end':
            continue
        if v not in map_steps:
            map_steps[v].append(key)
        if key not in map_steps[v]:
            map_steps[v].append(key)
print(map_steps)


counter = 0


def next_room(start, crumbs, visits):
    global counter
    new_visits = visits.copy()
    new_crumbs = crumbs.copy()
    new_crumbs.append(start)
    rooms = map_steps[start]
    # print(f"NEXT {rooms}")
    for r in rooms:
        add_lower = []
        # print(f" CHECKING {r}")
        if r == 'end':
            print(new_crumbs + ['end'])
            counter += 1
            continue
        elif r in visits:
            continue
        elif r.islower():
            # new_visits.append(r)
            add_lower = [r]

        next_room(r, new_crumbs, new_visits + add_lower)


next_room('start', [], [])
print(counter)
