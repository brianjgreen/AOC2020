#
# Advent of Code 2020 - Day 3 Part 1
# 3 Dec 2020 Brian Green
#
# Problem:
# From your starting position at the top-left, check the position that is right 3 and down 1.
# Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
#
import os


class Aoc03:
    def __init__(self):
        self.open = "."
        self.tree = "#"
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
    solve_it = Aoc03()
    solve_it.run_it()
