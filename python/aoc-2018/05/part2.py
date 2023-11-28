# Advent of Code 2018 - Day 5 Part 2
# 23 Oct 2023 Brian Green
#
# Problem:
# What is the length of the shortest polymer you can produce?
#

import string

from part1 import get_data


def get_poly_size(data_set):
    orig_poly = data_set
    short_poly = len(orig_poly)
    for element in string.ascii_lowercase:
        print(element, end="", flush=True)
        smallest = False
        lower_set = orig_poly.replace(element, "")
        data_set = lower_set.replace(element.upper(), "")
        while not smallest:
            smallest = True
            ptr = 0
            new_str = ""
            while ptr < len(data_set) - 1:
                curr = data_set[ptr]
                next = data_set[ptr + 1]
                if curr.lower() == next.lower() and curr != next:
                    smallest = False
                    ptr += 2
                else:
                    ptr += 1
                    new_str += curr
            data_set = new_str + next

            poly_size = len(data_set)
            if poly_size < short_poly:
                short_poly = poly_size
    print()
    return short_poly


if __name__ == "__main__":
    print(get_poly_size(get_data()[0]))
