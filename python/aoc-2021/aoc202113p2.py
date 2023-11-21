# Advent of Code 2021 - Day 13 Part 2
# 21 Nov 2023 Brian Green
#
# Problem: What code do you use to activate the infrared thermal imaging camera system?
#

import os


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data" + os.sep + "brian_aoc202113.dat"
    with open(filename) as data_file:
        data_set = [pos.strip() for pos in data_file.readlines()]

    return data_set


def plot_data(raw_data):
    """Read the raw data points and return a list of tuples with x and y coordinates of each dot"""
    dots = []
    for data in raw_data:
        if "," in data:
            x, y = data.split(",")
            dots.append((int(x), int(y)))
        else:
            break
    return dots


def get_folds(raw_data):
    """Read the raw data and extract and return a list of the folding instructions"""
    folds = []
    for data in raw_data:
        if "fold along" in data:
            folds.append(data.split()[2])
    return folds


def fold_paper(data, fold):
    """Fold the paper of plotted dots and return the newly folder paper list of coordinates of each dot"""
    folded_data = []
    axis, offset = fold.split("=")
    offset = int(offset)
    for dot in data:
        x, y = dot
        if axis == "x":
            new_y = y
            if x > offset:
                new_x = offset - (x - offset)
            else:
                new_x = x
        else:
            new_x = x
            if y > offset:
                new_y = offset - (y - offset)
            else:
                new_y = y
        if (new_x, new_y) not in folded_data:
            folded_data.append((new_x, new_y))

    return folded_data


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
