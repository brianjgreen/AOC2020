#
# Advent of Code 2020 - Day 2 Part 2
# 2 Dec 2020 Brian Green
#
# Problem:
# Each policy actually describes two positions in the password, where 1 means the first character,
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
# Exactly one of these positions must contain the given letter.
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
import os
import re


class Aoc02:
    def __init__(self):
        # self.test_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        file_name = "data" + os.sep + "brian_aoc02.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = self.test_data
        self.data = data_set

    def run_it(self):
        total = 0
        pattern = re.compile(r"(\d+)-(\d+) ([a-z]): (\w+)")
        for secret in self.data:
            m = re.match(pattern, secret)
            # print(m.groups())
            pos1, pos2, token, password = m.groups()
            first_pos = int(pos1) - 1
            second_pos = int(pos2) - 1
            if (password[first_pos] == token) ^ (password[second_pos] == token):
                # print("Good!")
                total += 1
        print(f"Total: {total}")


if __name__ == "__main__":
    solve_it = Aoc02()
    solve_it.run_it()
