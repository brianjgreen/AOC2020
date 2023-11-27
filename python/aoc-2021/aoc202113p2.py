# Advent of Code 2021 - Day 13 Part 2
# 21 Nov 2023 Brian Green
#
# Problem: What code do you use to activate the infrared thermal imaging camera system?
#

from aoc202113p1 import fold_paper, get_data, get_folds, plot_data


def get_max_dimensions(data):
    """Find and return the max x and y coordinates"""
    max_x = 0
    max_y = 0
    for x, y in data:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return max_x, max_y


if __name__ == "__main__":
    raw_data = get_data()
    data = plot_data(raw_data)
    folds = get_folds(raw_data)

    for fold_instruction in folds:
        data = fold_paper(data, fold_instruction)

    max_x, max_y = get_max_dimensions(data)
    print(f"max_x={max_x}, max_y={max_y}")

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in data:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print("")
