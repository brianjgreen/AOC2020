#
# Advent of Code 2020 - Day 12 Part 1
# 12 Dec 2020 Brian Green
#
# Problem:
# Figure out where the navigation instructions lead.
# What is the Manhattan distance between that location and the ship's starting position?
#
import os


class Aoc12:
    def __init__(self):
        self.north = 'N'
        self.south = 'S'
        self.east = 'E'
        self.west = 'W'
        self.left = 'L'
        self.right = 'R'
        self.forward = 'F'
        self.movement = {
            self.north: (-1, 0), self.south: (1, 0), self.east: (0, 1), self.west: (0, -1)
        }
        self.rotate_right = [self.east, self.south, self.west, self.north]
        self.rotate_left = [self.east, self.north, self.west, self.south]
        test_data = ["F10", "N3", "F7", "R90", "F11"]
        file_name = "data" + os.sep + "brian_aoc12.dat"
        with open(file_name) as data_file:
            data_set = [x.strip() for x in data_file.readlines()]

        # self.data = test_data
        self.data = data_set

    def run_it(self):
        x = 0
        y = 0
        facing = self.east
        for i in self.data:
            dir = i[0]
            dist = int(i[1:])

            if dir == self.left:
                facing = self.rotate_left[(self.rotate_left.index(facing) + int(dist/90)) % len(self.rotate_left)]
            elif dir == self.right:
                facing = self.rotate_right[(self.rotate_right.index(facing) + int(dist/90)) % len(self.rotate_right)]
            elif dir == self.forward:
                x_adj, y_adj = self.movement[facing]
                x += x_adj * dist
                y += y_adj * dist
            else:
                x_adj, y_adj = self.movement[dir]
                x += x_adj * dist
                y += y_adj * dist

            print(f"{facing} {x} {y}")
        print(f"M-Dist={abs(x) + abs(y)}")


if __name__ == "__main__":
    solve_it = Aoc12()
    solve_it.run_it()
