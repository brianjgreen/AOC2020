#
# Advent of Code 2020 - Day 2 Part 1
# 2 Dec 2020 Brian Green
#
# Problem:
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times a given letter must appear for the password
# to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
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
            mini, maxi, token, password = m.groups()
            minimum = int(mini)
            maximum = int(maxi)
            count = password.count(token)
            if minimum <= count <= maximum:
                # print("GOOD!")
                total += 1
        print(f"Total: {total}")


if __name__ == "__main__":
    solve_it = Aoc02()
    solve_it.run_it()
