#
# Advent of Code 2020 - Day 1 Part 2
# 1 Dec 2020 Brian Green
#
# Problem:
# The Elves in accounting are thankful for your help;
# one of them even offers you a starfish coin they had left over from a past vacation.
# They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
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
            third_pos = position + 1
            for y in self.data[position:]:
                for z in self.data[third_pos:]:
                    x = int(x)
                    y = int(y)
                    z = int(z)

                    print(f"{x}+{y}+{z}={x + y + z}")
                    if (x + y + z) == 2020:
                        print(f"FOUND IT {x * y * z}")
                        sys.exit()
                third_pos += 1
            position += 1


if __name__ == "__main__":
    solve_it = Aoc01()
    solve_it.run_it()
