# Advent of Code 2018 - Day 1 Part 2
# 19 Oct 2023 Brian Green
#
# Problem:
# Which frequency does it reach twice?
#

from part1 import get_data


def get_freq_found_twice(data_set):
    freq = 0
    all_freqs = []
    while True:
        for adjust in data_set:
            num = adjust[1:]
            if adjust[0] == "-":
                freq -= int(num)
            else:
                freq += int(num)
            if freq in all_freqs:
                return freq
            else:
                all_freqs.append(freq)


if __name__ == "__main__":
    print(get_freq_found_twice(get_data()))
