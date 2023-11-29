# Advent of Code 2017 - Day 1 Part 2
# 28 Nov 2023 Brian Green
#
# Problem:
# What is the solution to your new captcha?
#

from part1 import get_data


def get_sum_of_dupes_halfway(data_set):
    total = 0
    data_size = len(data_set)
    halfway = int(data_size / 2)
    for ptr in range(data_size - 1):
        half_ptr = (ptr + halfway) % data_size
        if data_set[ptr] == data_set[half_ptr]:
            total += int(data_set[ptr])

    return total


if __name__ == "__main__":
    raw_data = get_data()[0]
    print(get_sum_of_dupes_halfway(raw_data))
