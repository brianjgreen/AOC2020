# Advent of Code 2022 - Day 3 Part 1
# 19 Oct 2023 Brian Green
#
# Problem:
# How many square inches of fabric are within two or more claims?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_fabric(data_set):
    fabric = {}
    claim = {}  # for part 2
    for patch in data_set:
        cloth = patch.split()
        x_start, y_start = cloth[2][:-1].split(",")
        x_start = int(x_start)
        y_start = int(y_start)
        x_len, y_len = cloth[3].split("x")
        x_len = int(x_len)
        y_len = int(y_len)
        claim[cloth[0]] = []  # for part 2
        for x_offset in range(x_len):
            for y_offset in range(y_len):
                square = (x_start + x_offset, y_start + y_offset)
                claim[cloth[0]].append(square)  # for part 2
                if square in fabric:
                    fabric[square] += 1
                else:
                    fabric[square] = 1

    return fabric, claim


def find_overlap(fabric):
    overlap = 0
    for square in fabric:
        if fabric[square] > 1:
            overlap += 1

    return overlap


if __name__ == "__main__":
    fabric, claim = get_fabric(get_data())  # ignore claim for part 1
    print(find_overlap(fabric))
