#
# Advent of Code 2020 - Day 3 Part 1
# 3 Dec 2020 Brian Green
#
# Problem:
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times a given letter must appear for the password
# to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
import os


class Aoc02:
    def __init__(self):
        self.open = '.'
        self.tree = '#'
        self.x_offset = 3
        self.y_offset = 1
        """
        test_data = ["..##.......",
                     "#...#...#..",
                     ".#....#..#.",
                     "..#.#...#.#",
                     ".#...##..#.",
                     "..#.##.....",
                     ".#.#.#....#",
                     ".#........#",
                     "#.##...#...",
                     "#...##....#",
                     ".#..#...#.#"]
        """
        file_name = "data" + os.sep + "brian_aoc03.dat"
        with open(file_name) as data_file:
            data_set = data_file.readlines()

        # self.data = test_data
        self.data = data_set
        self.x_max = len(self.data[0].strip())
        self.y_max = len(self.data)

    def run_it(self):
        # print(self.x_max)
        # print(self.y_max)
        x = 0
        total_trees = 0
        for y in range(0, self.y_max, self.y_offset):
            location = self.data[y][x]
            if location == self.tree:
                total_trees += 1
            # print(f"{x}, {y} {self.data[y][x]}")
            x += self.x_offset
            x %= self.x_max
        print(f"Total trees: {total_trees}")


if __name__ == "__main__":
    solve_it = Aoc02()
    solve_it.run_it()
