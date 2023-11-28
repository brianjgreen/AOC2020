# Advent of Code 2018 - Day 2 Part 1
# 19 Oct 2023 Brian Green
#
# Problem:
# What is the checksum?
#


def get_data():
    """Read the data file and return a list of stripped strings of each line"""
    filename = "data.dat"
    with open(filename) as data_file:
        data_set = [num.strip() for num in data_file.readlines()]

    return data_set


def get_duo_and_trio(data_set):
    num_doubles = 0
    num_triples = 0
    for box in data_set:
        found_double = False
        found_triple = False
        for id in box:
            count = box.count(id)
            if count == 2:
                found_double = True
            elif count == 3:
                found_triple = True
        if found_double:
            num_doubles += 1
        if found_triple:
            num_triples += 1

    return num_doubles, num_triples


if __name__ == "__main__":
    num_doubles, num_triples = get_duo_and_trio(get_data())
    print(num_doubles * num_triples)
