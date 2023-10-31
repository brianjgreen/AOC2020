#
# Advent of Code 2016 - Day 4 Part 1
# 11 May 2022 Brian Green
#
# Problem:
#

import os
from collections import Counter

filename = "data" + os.sep + "brian_aoc201604.dat"
with open(filename) as data_file:
    data_set = data_file.readlines()

print(data_set)

test1 = "aaaaa-bbb-z-y-x-123[abxyz]"

conn = test1.split("-")
checksum = conn[-1]
print(checksum)
room = "".join(sorted(conn[:-1]))
print(room)
print(Counter(room).most_common(5))
