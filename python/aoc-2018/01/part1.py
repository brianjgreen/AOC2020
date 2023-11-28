# Advent of Code 2018 - Day 1 Part 1
# 19 Oct 2023 Brian Green
#
# Problem:
# What is the resulting frequency?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_freq(data_set):
    freq = 0
    for adjust in data_set:
        num = adjust[1:]
        if adjust[0] == "-":
            freq -= int(num)
        else:
            freq += int(num)
    return freq


if __name__ == "__main__":
    print(get_freq(get_data()))
