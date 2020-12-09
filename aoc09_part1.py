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
        self.test_data = [35,
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
                          576]
        file_name = "data" + os.sep + "brian_aoc09.dat"
        with open(file_name) as data_file:
            data_set = [int(x) for x in data_file.readlines()]

        self.data = self.test_data
        self.preamble = 5
        # self.data = data_set
        # self.preamble = 25

    def run_it(self):
        for i in range(self.preamble, len(self.data)):
            valid = False
            print(f"{i} {self.data[i]}")
            for j in range(i - self.preamble, i):
                # print(j)
                for k in range(j + 1, i):
                    print(f"{self.data[i]}: {self.data[j]}+{self.data[k]}={self.data[j]+self.data[k]}")
                    if self.data[j] != self.data[k] and self.data[j] + self.data[k] == self.data[i]:
                        print("GOOD")
                        valid = True
            if valid is False:
                print(f"{self.data[i]} is bad")
                sys.exit()


if __name__ == "__main__":
    solve_it = Aoc01()
    solve_it.run_it()
