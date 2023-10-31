#
# Advent of Code 2020 - Day 10 Part 1
# 10 Dec 2020 Brian Green
#
# Problem:
#
#
import os


class Aoc10:
    def __init__(self):
        self.test_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        self.test_data_2 = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
        ]
        file_name = "data" + os.sep + "brian_aoc10.dat"
        with open(file_name) as data_file:
            data_set = [int(x) for x in data_file.readlines()]

        # self.data = self.test_data
        # self.data = self.test_data_2
        self.data = data_set

    def run_it(self):
        diff = {1: 0, 2: 0, 3: 1}
        self.data.sort()
        print(self.data)
        diff[self.data[0]] = 1
        for i in range(1, len(self.data)):
            # print(f"{self.data[i]} {self.data[i-1]}")
            diff[self.data[i] - self.data[i - 1]] += 1

        print(diff)
        print(diff[1] * diff[3])


if __name__ == "__main__":
    solve_it = Aoc10()
    solve_it.run_it()
