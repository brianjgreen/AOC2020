#
# Advent of Code 2020 - Day 6 Part 2
# 6 Dec 2020 Brian Green
#
# Problem:
# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
#
import os


class Aoc06:
    def __init__(self):
        self.alpha = "abcdefghijklmnopqrstuvwxyz"
        # test_data = ["abc\n", "\n", "a\n", "b\n", "c\n", "\n", "ab\n", "ac\n", "\n", "a\n", "a\n", "a\n", "a\n", "\n",
        #              "b\n", "\n"]

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
                # Check each answer line (person) in the group of questions
                for j in questions:
                    # Check each possible answer (a-z)
                    for answered_yes in self.alpha:
                        if answered_yes in j:
                            # Count each answer in a group
                            if answered_yes in group_ans:
                                group_ans[answered_yes] = group_ans[answered_yes] + 1
                            else:
                                group_ans[answered_yes] = 1

                # Check all of the questions answered yes in a group
                for answer in group_ans:
                    if group_ans[answer] == len(questions):
                        # Number of yes answers matches the number of people in the group
                        count += 1
                questions = []
            else:
                questions.append(i)

        print(count)


if __name__ == "__main__":
    solve_it = Aoc06()
    solve_it.run_it()
