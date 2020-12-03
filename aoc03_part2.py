#
# Advent of Code 2020 - Day 3 Part 2
# 3 Dec 2020 Brian Green
#
# Problem:
# Determine the number of trees you would encounter if, for each of the following slopes,
# you start at the top-left corner and traverse the map all the way to the bottom:
#
import os


class Aoc02:
    def __init__(self):
        self.slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        self.open = '.'
        self.tree = '#'
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
        big_num = 1
        for x, y in self.slopes:
            print(f"{x}, {y}")
            curr_trees = self.get_num_trees(x, y)
            big_num *= curr_trees
        print(f"Big number: {big_num}")

    # Input x slope and y slope.
    # Returns the number of trees encountered
    def get_num_trees(self, x_offset, y_offset):
        x = 0
        total_trees = 0
        for y in range(0, self.y_max, y_offset):
            location = self.data[y][x]
            if location == self.tree:
                total_trees += 1
            # print(f"{x}, {y} {self.data[y][x]}")
            x += x_offset
            x %= self.x_max
        print(f"Total trees: {total_trees}")
        return total_trees


if __name__ == "__main__":
    solve_it = Aoc02()
    solve_it.run_it()
