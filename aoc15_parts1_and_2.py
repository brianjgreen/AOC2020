#
# Advent of Code 2020 - Day 15 Parts 1 and 2
# 15 Dec 2020 Brian Green
#
# Problem:
# Part 1: Given your starting numbers, what will be the 2020th number spoken?
# Part 2: Given your starting numbers, what will be the 30000000th number spoken?
#
import os


class Aoc15:
    def __init__(self):
        test_data = [0, 3, 6]  # 436
        test_data1 = [1, 3, 2]  # 1 
        test_data2 = [2, 1, 3]  # 10
        test_data3 = [1, 2, 3]  # 27
        test_data4 = [2, 3, 1]  # 78
        test_data5 = [3, 2, 1]  # 438
        test_data6 = [3, 1, 2]  # 1836

        data_set = [0, 12, 6, 13, 20, 1, 17]

        # self.data = test_data
        self.data = data_set

        self.part1_max_turn = 2020
        self.part2_max_turn = 30000000

    def run_it(self):
        turn = 1
        history = {}
        for num in self.data:
            history[num] = turn
            turn += 1

        num = 0
        while turn < self.part2_max_turn:
            if num in history:
                new_num = turn - history[num]
            else:
                new_num = 0
            history[num] = turn
            num = new_num
            turn += 1
        print(f"{turn} {num}")


if __name__ == "__main__":
    solve_it = Aoc15()
    solve_it.run_it()
