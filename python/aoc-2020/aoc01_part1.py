#
# Advent of Code 2020 - Day 1 Part 1
# 1 Dec 2020 Brian Green
#
# Problem:
# The Elves in accounting just need you to fix your expense report (your puzzle input);
# apparently, something isn't quite adding up.
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
#
import os
import sys


class Aoc01:
    def __init__(self):
        self.test_data = [1721, 979, 366, 299, 675, 1456]
        file_name = "data" + os.sep + "brian_aoc01.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = self.test_data
        self.data = data_set

    def run_it(self):
        position = 1
        for x in self.data:
            for y in self.data[position:]:
                x = int(x)
                y = int(y)
                print(f"{x}+{y}={x + y}")
                if (x + y) == 2020:
                    print(f"FOUND IT {x * y}")
                    sys.exit()

            position += 1


if __name__ == "__main__":
    solve_it = Aoc01()
    solve_it.run_it()
