# Advent of Code 2022 - Day 3 Part 2
# 19 Oct 2023 Brian Green
#
# Problem:
# What is the ID of the only claim that doesn't overlap?
#

from part1 import get_data, get_fabric


def get_patch(fabric, claim):
    for patch, coord in claim.items():
        clean = True
        for square in coord:
            if fabric[square] > 1:
                clean = False
        if clean:
            return patch
    print("Failed to find patch!")
    return None


if __name__ == "__main__":
    fabric, claim = get_fabric(get_data())
    print(get_patch(fabric, claim))
