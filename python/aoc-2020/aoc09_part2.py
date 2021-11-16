#
# Advent of Code 2020 - Day 1 Part 1
# 1 Dec 2020 Brian Green
#
# Problem:
# To find the encryption weakness, add together the smallest and largest number in this contiguous range.
# What is the encryption weakness in your XMAS-encrypted list of numbers?
#
import os
import sys


class Aoc09:
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

        # self.data = self.test_data
        # self.preamble = 5
        self.data = data_set
        self.preamble = 25

    def run_get_bad(self):
        bad = 0
        for i in range(self.preamble, len(self.data)):
            valid = False
            for j in range(i - self.preamble, i):
                for k in range(j + 1, i):
                    # print(f"{self.data[i]}: {self.data[j]}+{self.data[k]}={self.data[j]+self.data[k]}")
                    if self.data[j] != self.data[k] and self.data[j] + self.data[k] == self.data[i]:
                        print("GOOD")
                        valid = True
            if valid is False:
                bad = self.data[i]
                print(f"{bad} is bad")
                return bad

    def run_it(self):
        bad = self.run_get_bad()
        print("Thinking...")
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                total = 0
                for k in range(i, j):
                    total += self.data[k]
                    if total == bad:
                        checksum = []
                        for hack in range(i, j):
                            checksum.append(self.data[hack])
                            print(self.data[hack])
                        print(checksum.sort())
                        print(f"low:{checksum[0]} high:{checksum[-1]} sum:{checksum[0] + checksum[-1]}")
                        sys.exit()


if __name__ == "__main__":
    solve_it = Aoc09()
    solve_it.run_it()
