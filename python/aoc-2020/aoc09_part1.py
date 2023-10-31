#
# Advent of Code 2020 - Day 1 Part 1
# 1 Dec 2020 Brian Green
#
# Problem:
# The first step of attacking the weakness in the XMAS data is to find the first number in the list
# (after the preamble) which is not the sum of two of the 25 numbers before it.
# What is the first number that does not have this property?
#
import os
import sys


class Aoc09:
    def __init__(self):
        self.test_data = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
        ]
        file_name = "data" + os.sep + "brian_aoc09.dat"
        with open(file_name) as data_file:
            data_set = [int(x) for x in data_file.readlines()]

        # self.data = self.test_data
        # self.preamble = 5
        self.data = data_set
        self.preamble = 25

    def run_it(self):
        for i in range(self.preamble, len(self.data)):
            valid = False
            for j in range(i - self.preamble, i):
                for k in range(j + 1, i):
                    # print(f"{self.data[i]}: {self.data[j]}+{self.data[k]}={self.data[j]+self.data[k]}")
                    if (
                        self.data[j] != self.data[k]
                        and self.data[j] + self.data[k] == self.data[i]
                    ):
                        # print("GOOD")
                        valid = True
            if valid is False:
                print(f"{self.data[i]} is bad")
                sys.exit()


if __name__ == "__main__":
    solve_it = Aoc09()
    solve_it.run_it()
