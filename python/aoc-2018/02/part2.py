# Advent of Code 2018 - Day 2 Part 2
# 20 Oct 2023 Brian Green
#
# Problem:
# What letters are common between the two correct box IDs?
#

from difflib import SequenceMatcher

# filename = "test.dat"
filename = "data.dat"
with open(filename) as data_file:
    data_set = [num.strip() for num in data_file.readlines()]

comp_ratio = 0
best_match = None
while len(data_set) > 1:
    test_str = data_set.pop()
    for box in data_set:
        this_ratio = SequenceMatcher(None, test_str, box).ratio()
        if this_ratio > comp_ratio:
            best_match = (test_str, box)
            comp_ratio = this_ratio

print(comp_ratio)
print(best_match)
str1, str2 = best_match
common_str = ""
for x in range(len(str1)):
    if str1[x] == str2[x]:
        common_str += str1[x]
print(common_str)
