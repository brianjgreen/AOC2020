# Advent of Code 2017 - Day 1 Part 1
# 28 Nov 2023 Brian Green
#
# Problem:
# What is the solution to your captcha?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_sum_of_dupes(data_set):
    total = 0
    for ptr in range(len(data_set) - 1):
        if data_set[ptr] == data_set[ptr + 1]:
            total += int(data_set[ptr])

    return total


if __name__ == "__main__":
    raw_data = get_data()[0]
    raw_data += raw_data[0]
    print(get_sum_of_dupes(raw_data))
