#
# Advent of Code 2020 - Day 6 Part 2
# 6 Dec 2020 Brian Green
#
# Problem:
#
import os


class Aoc06:
    def __init__(self):
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        test_data = ["abc\n", "\n", "a\n", "b\n", "c\n", "\n", "ab\n", "ac\n", "\n", "a\n", "a\n", "a\n", "a\n", "\n",
                     "b\n", "\n"]

        file_name = "data" + os.sep + "brian_aoc06.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = test_data
        self.data = data_set

    def run_it(self):
        questions = []
        count = 0
        for i in self.data:
            if len(i) == 1:
                group_ans = {}
                for j in questions:
                    for l in self.alpha:
                        if l in j:
                            if l in group_ans:
                                group_ans[l] = group_ans[l] + 1
                            else:
                                group_ans[l] = 1
                for q in group_ans:
                    if group_ans[q] == len(questions):
                        count += 1
                questions = []
            else:
                questions.append(i)

        print(count)


if __name__ == "__main__":
    solve_it = Aoc06()
    solve_it.run_it()
