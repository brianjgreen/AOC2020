# Advent of Code 2018 - Day 2 Part 2
# 20 Oct 2023 Brian Green
#
# Problem:
# What letters are common between the two correct box IDs?
#

from difflib import SequenceMatcher

from part1 import get_data


def get_best_match(data_set):
    comp_ratio = 0
    best_match = None
    while len(data_set) > 1:
        test_str = data_set.pop()
        for box in data_set:
            this_ratio = SequenceMatcher(None, test_str, box).ratio()
            if this_ratio > comp_ratio:
                best_match = (test_str, box)
                comp_ratio = this_ratio

    return best_match


def get_common_string(best_match):
    str1, str2 = best_match
    common_str = ""
    for x in range(len(str1)):
        if str1[x] == str2[x]:
            common_str += str1[x]

    return common_str


if __name__ == "__main__":
    best_match = get_best_match(get_data())
    print(get_common_string(best_match))
