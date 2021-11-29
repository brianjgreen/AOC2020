
# Advent of Code 2015 - Day 12 Part 2
# 22 Nov 2021 Brian Green
#
# Problem:
# Ignore any object (and all of its children) which has any property with the value "red".
#

import json
import os
import re

filename = "data" + os.sep + "brian_aoc201512.dat"
with open(filename) as data_file:
    data_json = json.load(data_file)
# print(json.dumps(data_json, indent=4))


def clear_dict(d):
    for i in d.values():
        if isinstance(i, dict):
            clear_dict(i)
        elif isinstance(i, list):
            get_red(i)
        elif 'red' == i:
            d.clear()
            print("CLEAR")
            return True
    return False


def get_red(obj):
    for i in obj:
        if isinstance(i, dict):
            if clear_dict(i):
                continue
            get_red(i)
        elif isinstance(i, list):
            get_red(i)


get_red(data_json)
print(json.dumps(data_json, indent=4))
pattern = re.compile(r"-{0,1}\d+")
matches = re.findall(pattern, str(data_json))
# print(matches)

total = 0
for i in matches:
    total += int(i)

print(total)
