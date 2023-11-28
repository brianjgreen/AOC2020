# Advent of Code 2018 - Day 5 Part 1
# 20 Oct 2023 Brian Green
#
# Problem:
# How many units remain after fully reacting the polymer you scanned?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_num_units(data_set):
    smallest = False
    while not smallest:
        smallest = True
        ptr = 0
        new_str = ""
        next = ""
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

    return data_set


if __name__ == "__main__":
    print(len(get_num_units(get_data()[0])))
