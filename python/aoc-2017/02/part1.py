# Advent of Code 2017 - Day 2 Part 1
# 29 Nov 2023 Brian Green
#
# Problem:
# What is the checksum for the spreadsheet?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def split_data(data_set):
    # split strings and convert to a list of integers
    split_data = []
    for row in data_set:
        split_data.append([int(num) for num in row.split()])

    return split_data


def calc_checksum(data):
    checksum = 0
    for row in data:
        checksum += max(row) - min(row)
    return checksum


if __name__ == "__main__":
    data = split_data(get_data())
    print(calc_checksum(data))
